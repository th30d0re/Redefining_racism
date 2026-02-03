import { motion } from 'framer-motion';
import './VennDiagram.css';

interface VennDiagramProps {
  data: {
    inGroup: { label: string; members: string[] };
    outGroup: { label: string; members: string[] };
    elite?: { label: string; members: string[] };
  };
}

const VennDiagram = ({ data }: VennDiagramProps) => {
  return (
    <div className="venn-diagram">
      <svg viewBox="0 0 600 400" className="venn-svg">
        {/* Out-group circle */}
        <motion.circle
          cx="200"
          cy="200"
          r="120"
          fill="rgba(239, 68, 68, 0.3)"
          stroke="#ef4444"
          strokeWidth="3"
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ duration: 0.6, delay: 0.2 }}
        />
        
        {/* In-group circle */}
        <motion.circle
          cx="400"
          cy="200"
          r="120"
          fill="rgba(59, 130, 246, 0.3)"
          stroke="#3b82f6"
          strokeWidth="3"
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          transition={{ duration: 0.6, delay: 0.4 }}
        />

        {/* Elite circle (subset of In-group) */}
        {data.elite && (
          <motion.circle
            cx="420"
            cy="180"
            r="50"
            fill="rgba(168, 85, 247, 0.5)"
            stroke="#a855f7"
            strokeWidth="2"
            strokeDasharray="5,5"
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ duration: 0.6, delay: 0.6 }}
          />
        )}

        {/* Labels */}
        <motion.text
          x="200"
          y="100"
          textAnchor="middle"
          className="venn-label"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.8 }}
        >
          {data.outGroup.label}
        </motion.text>

        <motion.text
          x="400"
          y="100"
          textAnchor="middle"
          className="venn-label"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.0 }}
        >
          {data.inGroup.label}
        </motion.text>

        {data.elite && (
          <motion.text
            x="420"
            y="160"
            textAnchor="middle"
            className="venn-label elite"
            fontSize="12"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.2 }}
          >
            {data.elite.label}
          </motion.text>
        )}
      </svg>

      {/* Legend */}
      <div className="venn-legend">
        <div className="legend-section">
          <div className="legend-title">{data.outGroup.label}</div>
          <ul>
            {data.outGroup.members.map((member, idx) => (
              <motion.li
                key={idx}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.8 + idx * 0.1 }}
              >
                {member}
              </motion.li>
            ))}
          </ul>
        </div>

        <div className="legend-section">
          <div className="legend-title">{data.inGroup.label}</div>
          <ul>
            {data.inGroup.members.map((member, idx) => (
              <motion.li
                key={idx}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 1.0 + idx * 0.1 }}
              >
                {member}
              </motion.li>
            ))}
          </ul>
        </div>

        {data.elite && (
          <div className="legend-section">
            <div className="legend-title">{data.elite.label}</div>
            <ul>
              {data.elite.members.map((member, idx) => (
                <motion.li
                  key={idx}
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 1.2 + idx * 0.1 }}
                >
                  {member}
                </motion.li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default VennDiagram;
