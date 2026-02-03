import { useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { motion } from 'framer-motion';
import './OutgroupExpansion.css';

const OutgroupExpansion = () => {
  const svgRef = useRef<SVGSVGElement>(null);

  const data = [
    { year: 1619, size: 1, groups: ['Enslaved Africans'] },
    { year: 1705, size: 1.2, groups: ['Black people'] },
    { year: 1865, size: 2.5, groups: ['Black people', 'Poor whites (convict leasing)'] },
    { year: 1896, size: 2.8, groups: ['Black people', 'Poor whites', 'Immigrants'] },
    { year: 1971, size: 4.5, groups: ['Black people', 'Poor people', 'Drug users', 'Anti-war left'] },
    { year: 2020, size: 6.2, groups: ['Black people', 'Poor people', 'Drug users', 'Immigrants', 'Debtors', 'The incarcerated'] }
  ];

  useEffect(() => {
    if (!svgRef.current) return;

    const svg = d3.select(svgRef.current);
    const width = 800;
    const height = 400;
    const margin = { top: 40, right: 40, bottom: 60, left: 60 };

    svg.selectAll('*').remove();

    const xScale = d3
      .scaleLinear()
      .domain([1600, 2030])
      .range([margin.left, width - margin.right]);

    const yScale = d3
      .scaleLinear()
      .domain([0, 7])
      .range([height - margin.bottom, margin.top]);

    // Axes
    const xAxis = d3.axisBottom(xScale).tickFormat(d => d.toString());
    const yAxis = d3.axisLeft(yScale);

    svg
      .append('g')
      .attr('transform', `translate(0,${height - margin.bottom})`)
      .call(xAxis)
      .attr('class', 'axis');

    svg
      .append('g')
      .attr('transform', `translate(${margin.left},0)`)
      .call(yAxis)
      .attr('class', 'axis');

    // Axis labels
    svg
      .append('text')
      .attr('x', width / 2)
      .attr('y', height - 10)
      .attr('text-anchor', 'middle')
      .attr('class', 'axis-label')
      .text('Year');

    svg
      .append('text')
      .attr('transform', 'rotate(-90)')
      .attr('x', -height / 2)
      .attr('y', 15)
      .attr('text-anchor', 'middle')
      .attr('class', 'axis-label')
      .text('Out-group Size (|O(t)|)');

    // Line generator
    const line = d3
      .line<typeof data[0]>()
      .x(d => xScale(d.year))
      .y(d => yScale(d.size))
      .curve(d3.curveMonotoneX);

    // Draw line
    const path = svg
      .append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', '#ef4444')
      .attr('stroke-width', 3)
      .attr('d', line);

    // Animate line
    const totalLength = path.node()?.getTotalLength() || 0;
    path
      .attr('stroke-dasharray', `${totalLength} ${totalLength}`)
      .attr('stroke-dashoffset', totalLength)
      .transition()
      .duration(2000)
      .ease(d3.easeLinear)
      .attr('stroke-dashoffset', 0);

    // Points
    svg
      .selectAll('.data-point')
      .data(data)
      .enter()
      .append('circle')
      .attr('class', 'data-point')
      .attr('cx', d => xScale(d.year))
      .attr('cy', d => yScale(d.size))
      .attr('r', 0)
      .attr('fill', '#ef4444')
      .attr('stroke', '#fff')
      .attr('stroke-width', 2)
      .transition()
      .duration(300)
      .delay((d, i) => i * 350)
      .attr('r', 6);

  }, []);

  return (
    <div className="outgroup-expansion">
      <motion.svg
        ref={svgRef}
        viewBox="0 0 800 400"
        className="expansion-svg"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
      />

      <div className="expansion-details">
        {data.map((period, idx) => (
          <motion.div
            key={period.year}
            className="period-detail"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: idx * 0.3 }}
          >
            <div className="period-year">{period.year}</div>
            <div className="period-groups">
              {period.groups.map((group, gIdx) => (
                <span key={gIdx} className="group-tag">
                  {group}
                </span>
              ))}
            </div>
          </motion.div>
        ))}
      </div>

      <motion.div 
        className="theorem-box"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 1.5 }}
      >
        <h4>Out-group Expansion Theorem</h4>
        <code>|O(t)| is monotonically non-decreasing as t → ∞</code>
        <p>
          The oppressed class expands over time as the system requires an ever-growing 
          population to extract value from while maintaining elite power.
        </p>
      </motion.div>
    </div>
  );
};

export default OutgroupExpansion;
