import React, { useState, useEffect } from 'react';
import "../styles/LeaderboardScreen.css"; 
import { Link } from 'react-router-dom';

const LeaderboardTable = ({ data, difficulty }) => (
  <div className="leaderboard-container">
    <h2 className='leaderboard-difficulty'>{difficulty}</h2>
    <table className="leaderboard-table">
      <thead>
        <tr>
          <th>Rank</th>
          <th>Player</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>
        {data.map((entry, index) => (
          <tr key={index}>
            <td>{entry.rank}</td>
            <td>{entry.playerName}</td>
            <td>{entry.score}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

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
        const sortedDataEasy = easyLeaderboardData.filter(entry => entry.score).sort((a, b) => b.score - a.score);
        const sortedDataNormal = normalLeaderboardData.filter(entry => entry.score).sort((a, b) => b.score - a.score);
        const sortedDataHard = hardLeaderboardData.filter(entry => entry.score).sort((a, b) => b.score - a.score);

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
        <div className="leaderboards-wrapper">
          <LeaderboardTable data={leaderboardData.easy} difficulty="Easy" />
          <LeaderboardTable data={leaderboardData.normal} difficulty="Normal" />
          <LeaderboardTable data={leaderboardData.hard} difficulty="Hard" />
        </div>
      )}
    </div>
  );
};

const easyLeaderboardData = [
  { playerName: 'Ryan', score: 1300},
  { playerName: 'Raj', score: 1800},
  { playerName: 'CJ', score: 1550},
  { playerName: 'Julia', score: 1630},
];  

const normalLeaderboardData = [
  { playerName: 'Kartik', score: 1200},
  { playerName: 'Kap', score: 1400},
  { playerName: 'Chris', score: 1740},
  { playerName: 'Rachel', score: 1900},
];

const hardLeaderboardData = [
  { playerName: 'Justin', score: 2000},
  { playerName: 'Rayyan', score: 1100},
  { playerName: 'Christian', score: 1970},
  { playerName: 'Jae', score: 1480},
  { playerName: 'Patty', score: 1750},
];

export default LeaderboardScreen;
