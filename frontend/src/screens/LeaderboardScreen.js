import React, { useState, useEffect } from 'react';
import "../LeaderboardScreen.css"; 

const LeaderboardScreen = () => {
  const [leaderboardData, setLeaderboardData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLeaderboardData = async () => {
      try {
        // Simulating the API call with the test dataset
        //Sort the scores
        const sortedData = testLeaderboardData.sort((a, b) => b.score - a.score);
        setLeaderboardData(sortedData);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching leaderboard data:', error);
        setLoading(false);
      }
    };
  
    fetchLeaderboardData();
  }, []);
  
  

  return (
    <div className="leaderboard-container">
      <h1 className="leaderboard-title">Leaderboard</h1>
      {loading ? (
        <p>Loading leaderboard...</p>
      ) : (
        <table className="leaderboard-table">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Player</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            {leaderboardData.map((entry, index) => (
              <tr key={index}>
                <td>{index + 1}</td>
                <td>{entry.playerName}</td>
                <td>{entry.score}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

const testLeaderboardData = [
    { playerName: 'Justin', score: 1500 },
    { playerName: 'Kartik', score: 1200 },
    { playerName: 'Rayyan', score: 1100 },
    { playerName: 'Ryan', score: 1300 },
    { playerName: 'Kap', score: 1400 },
    { playerName: 'Christian', score: 1250 },
  ];  

export default LeaderboardScreen;
