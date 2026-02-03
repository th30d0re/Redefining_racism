import { useState } from 'react';
import { motion } from 'framer-motion';
import './CompoundingMetrics.css';

const CompoundingMetrics = () => {
  const [selectedMetric, setSelectedMetric] = useState<'wealth' | 'incarceration' | 'health'>('incarceration');

  const metrics = {
    incarceration: {
      title: 'Incarceration Compounding',
      description: 'Each year of incarceration reduces future employment probability, increasing recidivism.',
      formula: 'P(employed | t years incarcerated) = P₀ × (0.7)^t',
      data: [
        { years: 0, probability: 100 },
        { years: 1, probability: 70 },
        { years: 2, probability: 49 },
        { years: 5, probability: 16.8 },
        { years: 10, probability: 2.8 }
      ]
    },
    wealth: {
      title: 'Wealth Gap Compounding',
      description: 'Historical wealth extraction creates exponentially diverging outcomes.',
      formula: 'W_gap(t) = W₀ × e^(rt) where r ≈ 0.05',
      data: [
        { years: 0, gap: 1 },
        { years: 50, gap: 12.2 },
        { years: 100, gap: 148.4 },
        { years: 150, gap: 1808.0 },
        { years: 200, gap: 22026.5 }
      ]
    },
    health: {
      title: 'Health Disparity Compounding',
      description: 'Stress from oppression accelerates aging and disease.',
      formula: 'Life expectancy gap ≈ 3.5 years (Black vs White Americans)',
      data: [
        { age: 0, gap: 0 },
        { age: 20, gap: 0.5 },
        { age: 40, gap: 1.5 },
        { age: 60, gap: 2.8 },
        { age: 80, gap: 3.5 }
      ]
    }
  };

  const currentMetric = metrics[selectedMetric];

  return (
    <div className="compounding-metrics">
      <div className="metric-selector">
        <button
          className={selectedMetric === 'incarceration' ? 'active' : ''}
          onClick={() => setSelectedMetric('incarceration')}
        >
          Incarceration
        </button>
        <button
          className={selectedMetric === 'wealth' ? 'active' : ''}
          onClick={() => setSelectedMetric('wealth')}
        >
          Wealth Gap
        </button>
        <button
          className={selectedMetric === 'health' ? 'active' : ''}
          onClick={() => setSelectedMetric('health')}
        >
          Health Disparity
        </button>
      </div>

      <motion.div
        key={selectedMetric}
        className="metric-content"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
      >
        <h3>{currentMetric.title}</h3>
        <p>{currentMetric.description}</p>
        
        <div className="formula">
          <code>{currentMetric.formula}</code>
        </div>

        <div className="chart">
          {currentMetric.data.map((point, idx) => {
            const maxValue = Math.max(...currentMetric.data.map(d => Object.values(d)[1] as number));
            const value = Object.values(point)[1] as number;
            const height = (value / maxValue) * 100;
            
            return (
              <motion.div
                key={idx}
                className="bar-container"
                initial={{ height: 0 }}
                animate={{ height: 'auto' }}
                transition={{ delay: idx * 0.1 }}
              >
                <motion.div
                  className="bar"
                  style={{ height: `${height}%` }}
                  initial={{ scaleY: 0 }}
                  animate={{ scaleY: 1 }}
                  transition={{ delay: idx * 0.1, duration: 0.4 }}
                >
                  <span className="bar-value">
                    {typeof value === 'number' ? value.toFixed(1) : value}
                  </span>
                </motion.div>
                <div className="bar-label">
                  {Object.keys(point)[0]}: {Object.values(point)[0]}
                </div>
              </motion.div>
            );
          })}
        </div>

        <div className="insight">
          <h4>Key Insight</h4>
          {selectedMetric === 'incarceration' && (
            <p>
              After 5 years of incarceration, employment probability drops to just 17%, 
              creating a nearly inescapable cycle of poverty and re-incarceration.
            </p>
          )}
          {selectedMetric === 'wealth' && (
            <p>
              Starting from the same initial wealth, 200 years of compounding at different 
              rates creates a gap of over 22,000x—explaining the persistent racial wealth gap.
            </p>
          )}
          {selectedMetric === 'health' && (
            <p>
              The chronic stress of navigating oppressive systems literally shortens lives, 
              with Black Americans living on average 3.5 years less than white Americans.
            </p>
          )}
        </div>
      </motion.div>
    </div>
  );
};

export default CompoundingMetrics;
