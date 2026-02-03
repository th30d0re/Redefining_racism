import { useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import * as d3 from 'd3';
import './Timeline.css';

interface TimelineEvent {
  year: number;
  event: string;
  outgroup: string[];
}

interface TimelineProps {
  data: TimelineEvent[];
}

const Timeline = ({ data }: TimelineProps) => {
  const svgRef = useRef<SVGSVGElement>(null);

  useEffect(() => {
    if (!svgRef.current) return;

    const svg = d3.select(svgRef.current);
    const width = 900;
    const height = 400;
    const margin = { top: 50, right: 50, bottom: 100, left: 50 };

    svg.selectAll('*').remove();

    const xScale = d3
      .scaleLinear()
      .domain([d3.min(data, d => d.year)! - 10, d3.max(data, d => d.year)! + 10])
      .range([margin.left, width - margin.right]);

    // Main timeline line
    svg
      .append('line')
      .attr('x1', margin.left)
      .attr('x2', width - margin.right)
      .attr('y1', height / 2)
      .attr('y2', height / 2)
      .attr('stroke', '#6b7280')
      .attr('stroke-width', 2);

    // Events
    data.forEach((event, idx) => {
      const x = xScale(event.year);
      const y = height / 2;
      const isEven = idx % 2 === 0;

      // Event line
      svg
        .append('line')
        .attr('x1', x)
        .attr('x2', x)
        .attr('y1', y)
        .attr('y2', isEven ? y - 60 : y + 60)
        .attr('stroke', '#ef4444')
        .attr('stroke-width', 2)
        .attr('opacity', 0)
        .transition()
        .duration(500)
        .delay(idx * 200)
        .attr('opacity', 1);

      // Event dot
      svg
        .append('circle')
        .attr('cx', x)
        .attr('cy', y)
        .attr('r', 6)
        .attr('fill', '#ef4444')
        .attr('stroke', '#fff')
        .attr('stroke-width', 2)
        .attr('opacity', 0)
        .transition()
        .duration(500)
        .delay(idx * 200)
        .attr('opacity', 1);

      // Year label
      svg
        .append('text')
        .attr('x', x)
        .attr('y', y + 25)
        .attr('text-anchor', 'middle')
        .attr('class', 'timeline-year')
        .text(event.year)
        .attr('opacity', 0)
        .transition()
        .duration(500)
        .delay(idx * 200)
        .attr('opacity', 1);

      // Event text
      const eventText = svg
        .append('text')
        .attr('x', x)
        .attr('y', isEven ? y - 70 : y + 70)
        .attr('text-anchor', 'middle')
        .attr('class', 'timeline-event')
        .attr('opacity', 0);

      // Wrap text
      const words = event.event.split(' ');
      let line: string[] = [];
      let lineNumber = 0;
      const lineHeight = 16;
      let tspan = eventText.append('tspan').attr('x', x).attr('dy', 0);

      words.forEach(word => {
        line.push(word);
        tspan.text(line.join(' '));
        if ((tspan.node()?.getComputedTextLength() || 0) > 150) {
          line.pop();
          tspan.text(line.join(' '));
          line = [word];
          tspan = eventText
            .append('tspan')
            .attr('x', x)
            .attr('dy', lineHeight)
            .text(word);
          lineNumber++;
        }
      });

      eventText
        .transition()
        .duration(500)
        .delay(idx * 200)
        .attr('opacity', 1);
    });
  }, [data]);

  return (
    <div className="timeline-container">
      <motion.svg
        ref={svgRef}
        viewBox="0 0 900 400"
        className="timeline-svg"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
      />
      
      <div className="timeline-outgroups">
        <h4>Expanding Out-groups:</h4>
        {data.map((event, idx) => (
          <motion.div
            key={idx}
            className="outgroup-entry"
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: idx * 0.2 }}
          >
            <strong>{event.year}:</strong> {event.outgroup.join(', ')}
          </motion.div>
        ))}
      </div>
    </div>
  );
};

export default Timeline;
