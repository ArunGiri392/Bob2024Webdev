// ScoresSection.js
import React from 'react';

const ScoresSection = () => {
  return (
    <section className="scores-section">
      <h2>Scores</h2>
      <ul>
        <li>Team A vs. Team B: 24-21</li>
        <li>Team C vs. Team D: 28-14</li>
        <li>Team E vs. Team F: 17-10</li>
        {/* Add more score items as needed */}
      </ul>
    </section>
  );
};

export default ScoresSection;
