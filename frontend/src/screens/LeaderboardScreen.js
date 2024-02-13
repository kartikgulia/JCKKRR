import React, { useState, useEffect } from 'react';
import "../styles/LeaderboardScreen.css"; 
import { Link } from 'react-router-dom';

const LeaderboardScreen = () => {
  const [leaderboardData, setLeaderboardData] = useState({
    easy: [],
    normal: [],
    hard: [],
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLeaderboardData = async () => {
      try {
        // Simulating the API call with the test dataset
        const sortedDataEasy = testLeaderboardData.filter(entry => entry.difficulty === 'easy').sort((a, b) => b.score - a.score);
        const sortedDataNormal = testLeaderboardData.filter(entry => entry.difficulty === 'normal').sort((a, b) => b.score - a.score);
        const sortedDataHard = testLeaderboardData.filter(entry => entry.difficulty === 'hard').sort((a, b) => b.score - a.score);

        setLeaderboardData({
          easy: sortedDataEasy.map((entry, index) => ({ ...entry, rank: index + 1 })),
          normal: sortedDataNormal.map((entry, index) => ({ ...entry, rank: index + 1 })),
          hard: sortedDataHard.map((entry, index) => ({ ...entry, rank: index + 1 })),
        });

        setLoading(false);
      } catch (error) {
        console.error('Error fetching leaderboard data:', error);
        setLoading(false);
      }
    };
  
    fetchLeaderboardData();
  }, []);

  return (
    <div className="leaderboard-screen">
      <Link to="/gameSelect" className="back-button">Back</Link>
      <h1 className="leaderboard-title">Leaderboard</h1>
      {loading ? (
        <p>Loading leaderboard...</p>
      ) : (
        <table className="leaderboard-table">
          <thead>
            <tr>
              <th colSpan="3">Easy</th>
              <th colSpan="3">Normal</th>
              <th colSpan="3">Hard</th>
            </tr>
            <tr>
              <th>Rank</th>
              <th>Player</th>
              <th>Score</th>
              <th>Rank</th>
              <th>Player</th>
              <th>Score</th>
              <th>Rank</th>
              <th>Player</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            {[...Array(Math.max(leaderboardData.easy.length, leaderboardData.normal.length, leaderboardData.hard.length))].map((_, index) => (
              <tr key={index}>
                <td>{leaderboardData.easy[index]?.rank}</td>
                <td>{leaderboardData.easy[index]?.playerName}</td>
                <td>{leaderboardData.easy[index]?.score}</td>
                <td>{leaderboardData.normal[index]?.rank}</td>
                <td>{leaderboardData.normal[index]?.playerName}</td>
                <td>{leaderboardData.normal[index]?.score}</td>
                <td>{leaderboardData.hard[index]?.rank}</td>
                <td>{leaderboardData.hard[index]?.playerName}</td>
                <td>{leaderboardData.hard[index]?.score}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

const testLeaderboardData = [
  { playerName: 'Justin', score: 2000, difficulty: 'hard' },
  { playerName: 'Kartik', score: 1200, difficulty: 'normal' },
  { playerName: 'Rayyan', score: 1100, difficulty: 'hard' },
  { playerName: 'Ryan', score: 1300, difficulty: 'easy' },
  { playerName: 'Kap', score: 1400, difficulty: 'normal' },
  { playerName: 'Christian', score: 1970, difficulty: 'hard' },
  { playerName: 'Jae', score: 1480, difficulty: 'hard' },
  { playerName: 'Raj', score: 1800, difficulty: 'easy' },
  { playerName: 'CJ', score: 1550, difficulty: 'easy' },
  { playerName: 'Chris', score: 1740, difficulty: 'normal' },
  { playerName: 'Rachel', score: 1900, difficulty: 'normal' },
  { playerName: 'Julia', score: 1630, difficulty: 'easy' },
  { playerName: 'Patty', score: 1750, difficulty: 'hard' },
];  

export default LeaderboardScreen;
