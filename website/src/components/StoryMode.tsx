import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { storyChapters, type VennDiagramData, type TimelineEvent } from '../data/storyData';
import VennDiagram from './visualizations/VennDiagram';
import Timeline from './visualizations/Timeline';
import './StoryMode.css';

interface StoryModeProps {
  onComplete: () => void;
}

const StoryMode = ({ onComplete }: StoryModeProps) => {
  const [currentChapter, setCurrentChapter] = useState(0);
  const [progress, setProgress] = useState(0);
  const navigate = useNavigate();

  const chapter = storyChapters[currentChapter];

  useEffect(() => {
    setProgress((currentChapter / storyChapters.length) * 100);
  }, [currentChapter]);

  const handleNext = () => {
    if (currentChapter < storyChapters.length - 1) {
      setCurrentChapter(prev => prev + 1);
    } else {
      onComplete();
      navigate('/dashboard');
    }
  };

  const handlePrevious = () => {
    if (currentChapter > 0) {
      setCurrentChapter(prev => prev - 1);
    }
  };

  return (
    <div className="story-mode">
      {/* Progress Bar */}
      <div className="progress-bar">
        <motion.div 
          className="progress-fill"
          initial={{ width: 0 }}
          animate={{ width: `${progress}%` }}
          transition={{ duration: 0.5 }}
        />
      </div>

      {/* Story Content */}
      <AnimatePresence mode="wait">
        <motion.div
          key={currentChapter}
          initial={{ opacity: 0, x: 100 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -100 }}
          transition={{ duration: 0.5 }}
          className="chapter-container"
        >
          <div className="chapter-header">
            <h1>{chapter.title}</h1>
            <p className="chapter-number">Chapter {currentChapter + 1} of {storyChapters.length}</p>
          </div>

          <div className="chapter-content">
            {chapter.content.map((paragraph, idx) => (
              <motion.p
                key={idx}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: idx * 0.1 }}
              >
                {paragraph}
              </motion.p>
            ))}

            {/* Visualization */}
            {chapter.visualization === 'venn' && chapter.visualizationData && (
              <VennDiagram data={chapter.visualizationData as VennDiagramData} />
            )}
            {chapter.visualization === 'timeline' && chapter.visualizationData && (
              <Timeline data={chapter.visualizationData as TimelineEvent[]} />
            )}

            {/* Key Concepts */}
            {chapter.keyConcepts && (
              <div className="key-concepts">
                <h3>Key Concepts</h3>
                <ul>
                  {chapter.keyConcepts.map((concept, idx) => (
                    <motion.li
                      key={idx}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: 0.5 + idx * 0.1 }}
                    >
                      <strong>{concept.term}:</strong> {concept.definition}
                    </motion.li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          {/* Navigation */}
          <div className="chapter-navigation">
            <button 
              onClick={handlePrevious} 
              disabled={currentChapter === 0}
              className="nav-button"
            >
              ← Previous
            </button>
            <button 
              onClick={handleNext}
              className="nav-button primary"
            >
              {currentChapter === storyChapters.length - 1 ? 'Enter Dashboard →' : 'Next →'}
            </button>
          </div>
        </motion.div>
      </AnimatePresence>
    </div>
  );
};

export default StoryMode;
