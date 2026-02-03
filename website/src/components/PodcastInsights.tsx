import { useState } from 'react';
import { motion } from 'framer-motion';
import './PodcastInsights.css';

const PodcastInsights = () => {
  const [expandedSection, setExpandedSection] = useState<number | null>(null);

  const insights = [
    {
      title: 'Racism as Engineering, Not Essence',
      quote: '"Racism is an engineering problem, not a biological or cultural essence."',
      explanation: 'The podcast reveals that American racism was deliberately engineered in 1705 to solve a labor control problem. It wasn\'t an ancient tribal hatred—it was a calculated solution to prevent poor whites and enslaved Africans from uniting against the plantation elite.',
      keyPoint: 'This reframes racism from an irrational prejudice to a rational (though immoral) system designed to serve specific economic interests.'
    },
    {
      title: 'The Bacon\'s Rebellion Turning Point',
      quote: '"In 1676, poor whites and Black slaves united in Bacon\'s Rebellion, terrifying the colonial elite."',
      explanation: 'Before racial laws, class solidarity was the primary threat to power. The Virginia Slave Codes of 1705 granted poor whites symbolic privileges (gun ownership, ability to beat slaves) to fracture working-class unity along racial lines.',
      keyPoint: 'Racial division was the solution to class solidarity. This pattern repeats throughout American history.'
    },
    {
      title: 'The Nixon Drug War Confession',
      quote: '"We knew we were lying about the drugs... we could disrupt those communities and vilify them." - John Ehrlichman',
      explanation: 'Nixon\'s advisor openly admitted the War on Drugs was designed to criminalize political opposition (anti-war left and Black communities). The "drug crisis" was manufactured to justify mass incarceration.',
      keyPoint: 'Policy presented as public safety was actually political suppression with mathematical precision.'
    },
    {
      title: 'Mass Incarceration as Wealth Extraction',
      quote: '"The United States has 5% of the world\'s population but 25% of the world\'s prisoners."',
      explanation: 'Prison corporations, mandatory minimums, and convict labor create a system where incarceration generates profit. This explains why the Out-group must expand—the system requires an ever-growing supply of prisoners.',
      keyPoint: 'The carceral system is an economic engine disguised as criminal justice.'
    },
    {
      title: 'The Elite Benefit Model',
      quote: '"Poor whites aren\'t getting richer. The system serves a tiny Elite class, not the nominal In-group."',
      explanation: 'The podcast demonstrates that most white Americans don\'t benefit from systemic racism. Instead, a small Elite class (E ⊂ I) profits by keeping the majority divided. Poor whites gain symbolic status but lose economic solidarity.',
      keyPoint: 'Recognizing this creates the possibility for cross-racial working-class solidarity.'
    },
    {
      title: 'Micro-Scale Pattern Recognition',
      quote: '"The same four pillars appear in abusive relationships: asymmetric autonomy, selective empathy, ideological justification, resistance to critique."',
      explanation: 'The mathematical framework isn\'t limited to racial systems. Domestic abuse, toxic workplaces, and authoritarian regimes all follow the same architecture. This suggests oppression has a recognizable structure.',
      keyPoint: 'Understanding the pattern helps us identify oppression regardless of scale or context.'
    },
    {
      title: 'The Path Forward: Solidarity',
      quote: '"When we recognize that the system divides us to prevent solidarity, we can begin to build something better."',
      explanation: 'The podcast concludes that knowledge of the system\'s architecture is necessary but insufficient. The solution is solidarity across the artificial divisions the system creates.',
      keyPoint: 'Mathematical formalization enables recognition. Recognition enables resistance. Resistance enables change.'
    }
  ];

  return (
    <div className="podcast-insights">
      <div className="podcast-header">
        <h2>Podcast Deep Dive: Engineering Oppression</h2>
        <p>Key insights from "Racism is an Engineering Problem"</p>
      </div>

      <div className="insights-grid">
        {insights.map((insight, idx) => (
          <motion.div
            key={idx}
            className={`insight-card ${expandedSection === idx ? 'expanded' : ''}`}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: idx * 0.1 }}
            onClick={() => setExpandedSection(expandedSection === idx ? null : idx)}
          >
            <div className="insight-header">
              <h3>{insight.title}</h3>
              <span className="expand-icon">{expandedSection === idx ? '−' : '+'}</span>
            </div>

            <div className="insight-quote">
              {insight.quote}
            </div>

            {expandedSection === idx && (
              <motion.div
                className="insight-details"
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                exit={{ opacity: 0, height: 0 }}
                transition={{ duration: 0.3 }}
              >
                <div className="explanation">
                  <h4>Context</h4>
                  <p>{insight.explanation}</p>
                </div>
                <div className="key-point">
                  <h4>Key Takeaway</h4>
                  <p>{insight.keyPoint}</p>
                </div>
              </motion.div>
            )}
          </motion.div>
        ))}
      </div>

      <div className="podcast-cta">
        <h3>Want to go deeper?</h3>
        <p>The full podcast transcript explores these themes with additional historical examples and mathematical proofs.</p>
        <button className="cta-button">Read Full Transcript</button>
      </div>
    </div>
  );
};

export default PodcastInsights;
