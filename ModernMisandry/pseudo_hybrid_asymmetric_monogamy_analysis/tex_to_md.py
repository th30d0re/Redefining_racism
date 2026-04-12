#!/usr/bin/env python3
"""
LaTeX to Markdown Converter
Converts .tex files to .md format with reasonable fidelity.

Usage:
    python tex_to_md.py input.tex [output.md]
    
If output is not specified, it will use the same name as input with .md extension.
"""

import re
import sys
from pathlib import Path


def convert_tex_to_md(tex_content: str) -> str:
    """
    Convert LaTeX content to Markdown.
    
    Args:
        tex_content: The raw LaTeX file content
        
    Returns:
        Markdown formatted string
    """
    content = tex_content
    
    # Remove preamble (everything before \begin{document})
    doc_match = re.search(r'\\begin\{document\}', content)
    if doc_match:
        content = content[doc_match.end():]
    
    # Remove \end{document}
    content = re.sub(r'\\end\{document\}', '', content)
    
    # ============================================================
    # TITLE PAGE HANDLING
    # ============================================================
    
    # Extract title page content
    titlepage_match = re.search(r'\\begin\{titlepage\}(.*?)\\end\{titlepage\}', content, re.DOTALL)
    if titlepage_match:
        title_content = titlepage_match.group(1)
        # Extract the main title
        title_parts = re.findall(r'\{\\(?:LARGE|Large|large)\\bfseries\s+(.*?)\\par\}', title_content, re.DOTALL)
        if not title_parts:
            title_parts = re.findall(r'\\(?:LARGE|Large)\\bfseries\s+(.*?)\\par', title_content, re.DOTALL)
        
        md_title = "# "
        if title_parts:
            for part in title_parts:
                # Clean up the title
                cleaned = part.replace('\\\\', '\n').replace('[0.5em]', '').replace('[0.3em]', '')
                cleaned = re.sub(r'\\[a-zA-Z]+', '', cleaned)  # Remove remaining commands
                cleaned = cleaned.strip()
                md_title += cleaned + "\n"
        
        # Replace title page with markdown title
        content = content.replace(titlepage_match.group(0), md_title)
    
    # ============================================================
    # REMOVE LATEX COMMANDS WE DON'T NEED
    # ============================================================
    
    # Remove LaTeX comments (lines starting with %)
    content = re.sub(r'^%.*$', '', content, flags=re.MULTILINE)
    
    # Remove common non-content commands
    commands_to_remove = [
        r'\\newpage',
        r'\\tableofcontents',
        r'\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}',
        r'\\vspace\*?\{[^}]*\}',
        r'\\hspace\*?\{[^}]*\}',
        r'\\centering',
        r'\\noindent',
        r'\\clearpage',
        r'\\pagebreak',
        r'\\bigskip',
        r'\\medskip',
        r'\\smallskip',
        r'\\par',
        r'\\vfill',
        r'\\today',
        r'\\maketitle',
        r'\\label\{[^}]*\}',
    ]
    
    for cmd in commands_to_remove:
        content = re.sub(cmd, '', content)
    
    # ============================================================
    # SECTIONS
    # ============================================================
    
    # Convert sections (handle starred versions too)
    content = re.sub(r'\\section\*?\{([^}]*)\}', r'\n\n## \1\n\n', content)
    content = re.sub(r'\\subsection\*?\{([^}]*)\}', r'\n\n### \1\n\n', content)
    content = re.sub(r'\\subsubsection\*?\{([^}]*)\}', r'\n\n#### \1\n\n', content)
    content = re.sub(r'\\paragraph\*?\{([^}]*)\}', r'\n\n##### \1\n\n', content)
    
    # ============================================================
    # TEXT FORMATTING
    # ============================================================
    
    # Bold text
    content = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', content)
    content = re.sub(r'\\bfseries\s*([^{}]+?)(?=\\|$|\n\n)', r'**\1**', content)
    
    # Italic text
    content = re.sub(r'\\textit\{([^}]*)\}', r'*\1*', content)
    content = re.sub(r'\\emph\{([^}]*)\}', r'*\1*', content)
    content = re.sub(r'\\textsl\{([^}]*)\}', r'*\1*', content)
    
    # Typewriter/code text
    content = re.sub(r'\\texttt\{([^}]*)\}', r'`\1`', content)
    content = re.sub(r'\\verb\|([^|]*)\|', r'`\1`', content)
    
    # Small caps (just render as regular text)
    content = re.sub(r'\\textsc\{([^}]*)\}', r'\1', content)
    
    # ============================================================
    # QUOTES AND SPECIAL CHARACTERS
    # ============================================================
    
    # LaTeX quotes
    content = re.sub(r"``", '"', content)
    content = re.sub(r"''", '"', content)
    content = re.sub(r"`", "'", content)
    
    # Blockquotes
    def convert_blockquote(match):
        quote_content = match.group(1).strip()
        lines = quote_content.split('\n')
        return '\n' + '\n'.join(['> ' + line.strip() for line in lines if line.strip()]) + '\n'
    
    content = re.sub(r'\\begin\{quote\}(.*?)\\end\{quote\}', convert_blockquote, content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{quotation\}(.*?)\\end\{quotation\}', convert_blockquote, content, flags=re.DOTALL)
    
    # Epigraph
    def convert_epigraph(match):
        quote = match.group(1).strip()
        author = match.group(2).strip() if match.group(2) else ''
        result = f'\n> *{quote}*\n'
        if author:
            result += f'> — {author}\n'
        return result
    
    content = re.sub(r'\\epigraph\{([^}]*)\}\{([^}]*)\}', convert_epigraph, content)
    
    # ============================================================
    # LISTS
    # ============================================================
    
    def convert_itemize(match):
        list_content = match.group(1)
        items = re.split(r'\\item\s*', list_content)
        result = '\n'
        for item in items:
            item = item.strip()
            if item:
                # Handle multi-line items
                lines = item.split('\n')
                result += f'- {lines[0].strip()}\n'
                for line in lines[1:]:
                    if line.strip():
                        result += f'  {line.strip()}\n'
        return result + '\n'
    
    def convert_enumerate(match):
        options = match.group(1) or ''
        list_content = match.group(2)
        items = re.split(r'\\item\s*', list_content)
        result = '\n'
        counter = 1
        for item in items:
            item = item.strip()
            if item:
                lines = item.split('\n')
                result += f'{counter}. {lines[0].strip()}\n'
                for line in lines[1:]:
                    if line.strip():
                        result += f'   {line.strip()}\n'
                counter += 1
        return result + '\n'
    
    # Process nested lists from inside out
    for _ in range(5):  # Handle up to 5 levels of nesting
        content = re.sub(r'\\begin\{itemize\}(.*?)\\end\{itemize\}', convert_itemize, content, flags=re.DOTALL)
        content = re.sub(r'\\begin\{enumerate\}(?:\[([^\]]*)\])?(.*?)\\end\{enumerate\}', convert_enumerate, content, flags=re.DOTALL)
    
    # ============================================================
    # THEOREM-LIKE ENVIRONMENTS
    # ============================================================
    
    theorem_envs = ['definition', 'proposition', 'theorem', 'corollary', 'lemma', 'proof', 'remark', 'example']
    
    for env in theorem_envs:
        def make_converter(env_name):
            def converter(match):
                title = match.group(1) if match.lastindex and match.group(1) else ''
                body = match.group(2) if match.lastindex >= 2 else match.group(1)
                env_title = env_name.capitalize()
                if title:
                    return f'\n\n**{env_title}** *({title})*: {body.strip()}\n\n'
                return f'\n\n**{env_title}**: {body.strip()}\n\n'
            return converter
        
        # With optional title
        content = re.sub(
            rf'\\begin\{{{env}\}}\[([^\]]*)\](.*?)\\end\{{{env}\}}',
            make_converter(env),
            content,
            flags=re.DOTALL
        )
        # Without title
        content = re.sub(
            rf'\\begin\{{{env}\}}(.*?)\\end\{{{env}\}}',
            lambda m, e=env: f'\n\n**{e.capitalize()}**: {m.group(1).strip()}\n\n',
            content,
            flags=re.DOTALL
        )
    
    # ============================================================
    # MATH
    # ============================================================
    
    # Display math
    content = re.sub(r'\\\[(.*?)\\\]', r'\n$$\1$$\n', content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}', r'\n$$\1$$\n', content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}', r'\n$$\1$$\n', content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{gather\*?\}(.*?)\\end\{gather\*?\}', r'\n$$\1$$\n', content, flags=re.DOTALL)
    
    # Inline math
    content = re.sub(r'\$([^$]+)\$', r'$\1$', content)
    
    # ============================================================
    # TABLES (simplified conversion)
    # ============================================================
    
    def convert_table(match):
        table_content = match.group(0)
        # Extract tabular content
        tabular_match = re.search(r'\\begin\{(?:tabular|longtable)\}\{[^}]*\}(.*?)\\end\{(?:tabular|longtable)\}', 
                                   table_content, re.DOTALL)
        if not tabular_match:
            return '\n[Table content]\n'
        
        rows = tabular_match.group(1)
        # Split by \\ or \hline
        row_list = re.split(r'\\\\|\\hline|\\toprule|\\midrule|\\bottomrule', rows)
        
        md_table = '\n'
        header_done = False
        for row in row_list:
            row = row.strip()
            if not row or row.startswith('%'):
                continue
            # Split cells by &
            cells = [cell.strip() for cell in row.split('&')]
            if cells and any(c for c in cells):
                md_table += '| ' + ' | '.join(cells) + ' |\n'
                if not header_done:
                    md_table += '|' + '|'.join(['---' for _ in cells]) + '|\n'
                    header_done = True
        
        return md_table + '\n'
    
    content = re.sub(r'\\begin\{table\}.*?\\end\{table\}', convert_table, content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{longtable\}.*?\\end\{longtable\}', convert_table, content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{tabular\}\{[^}]*\}(.*?)\\end\{tabular\}', convert_table, content, flags=re.DOTALL)
    
    # ============================================================
    # FIGURES
    # ============================================================
    
    def convert_figure(match):
        fig_content = match.group(1)
        # Try to extract image path
        img_match = re.search(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', fig_content)
        caption_match = re.search(r'\\caption\{([^}]*)\}', fig_content)
        
        img_path = img_match.group(1) if img_match else 'image'
        caption = caption_match.group(1) if caption_match else ''
        
        return f'\n![{caption}]({img_path})\n'
    
    content = re.sub(r'\\begin\{figure\}(?:\[[^\]]*\])?(.*?)\\end\{figure\}', convert_figure, content, flags=re.DOTALL)
    
    # ============================================================
    # CITATIONS AND REFERENCES
    # ============================================================
    
    # Citations - convert to readable format
    content = re.sub(r'\\citep?\{([^}]*)\}', r'[\1]', content)
    content = re.sub(r'\\citet?\{([^}]*)\}', r'[\1]', content)
    content = re.sub(r'\\cite\{([^}]*)\}', r'[\1]', content)
    content = re.sub(r'\\autocite\{([^}]*)\}', r'[\1]', content)
    content = re.sub(r'\\textcite\{([^}]*)\}', r'[\1]', content)
    
    # References (cross-references)
    content = re.sub(r'\\ref\{([^}]*)\}', r'[\1]', content)
    content = re.sub(r'\\eqref\{([^}]*)\}', r'([\1])', content)
    content = re.sub(r'\\pageref\{([^}]*)\}', r'[page \1]', content)
    
    # ============================================================
    # FOOTNOTES
    # ============================================================
    
    footnote_counter = [0]
    footnotes = []
    
    def convert_footnote(match):
        footnote_counter[0] += 1
        footnote_text = match.group(1)
        footnotes.append(f'[^{footnote_counter[0]}]: {footnote_text}')
        return f'[^{footnote_counter[0]}]'
    
    content = re.sub(r'\\footnote\{([^}]*)\}', convert_footnote, content)
    
    # Add footnotes at the end
    if footnotes:
        content += '\n\n---\n\n' + '\n'.join(footnotes)
    
    # ============================================================
    # HYPERLINKS
    # ============================================================
    
    content = re.sub(r'\\href\{([^}]*)\}\{([^}]*)\}', r'[\2](\1)', content)
    content = re.sub(r'\\url\{([^}]*)\}', r'<\1>', content)
    
    # ============================================================
    # SPECIAL CHARACTERS AND SYMBOLS
    # ============================================================
    
    # LaTeX special characters
    content = content.replace(r'\%', '%')
    content = content.replace(r'\$', '$')
    content = content.replace(r'\&', '&')
    content = content.replace(r'\#', '#')
    content = content.replace(r'\_', '_')
    content = content.replace(r'\{', '{')
    content = content.replace(r'\}', '}')
    content = content.replace(r'\textbackslash', '\\')
    
    # Dashes
    content = content.replace('---', '—')
    content = content.replace('--', '–')
    
    # Non-breaking space
    content = content.replace('~', ' ')
    
    # Ellipsis
    content = content.replace(r'\ldots', '...')
    content = content.replace(r'\dots', '...')
    
    # ============================================================
    # CLEAN UP REMAINING LATEX COMMANDS
    # ============================================================
    
    # Remove any remaining \command{} patterns (keep the content)
    content = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', content)
    
    # Remove any remaining \command patterns
    content = re.sub(r'\\[a-zA-Z]+', '', content)
    
    # ============================================================
    # WHITESPACE CLEANUP
    # ============================================================
    
    # Remove excessive blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # Remove trailing whitespace from lines
    content = '\n'.join(line.rstrip() for line in content.split('\n'))
    
    # Remove leading/trailing whitespace from document
    content = content.strip()
    
    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python tex_to_md.py input.tex [output.md]")
        print("\nConverts a LaTeX .tex file to Markdown .md format.")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)
    
    if not input_path.suffix == '.tex':
        print(f"Warning: Input file does not have .tex extension.")
    
    # Determine output path
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_suffix('.md')
    
    print(f"Converting: {input_path}")
    print(f"Output: {output_path}")
    
    # Read input file
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            tex_content = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # Convert
    md_content = convert_tex_to_md(tex_content)
    
    # Write output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)
    
    print(f"✓ Conversion complete!")
    print(f"  Lines in input: {len(tex_content.splitlines())}")
    print(f"  Lines in output: {len(md_content.splitlines())}")


if __name__ == '__main__':
    main()













