import React, { useState, useEffect } from 'react';
import "../styles/LeaderboardScreen.css"; 
import { Link } from 'react-router-dom';

const LeaderboardTable = ({ data, difficulty }) => (
  <div className="leaderboard-container">
    <h2 className="leaderboard-difficulty">{difficulty}</h2>
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
        // Fetch data from your Firestore database for Easy difficulty
        const easyResponse = await fetch('http://localhost:5000/easyleaderboard');
        const easyData = await easyResponse.json();
        
        // Convert to array and sort by score
        const easyArray = Object.values(easyData);
        const sortedEasyData = easyArray.filter(entry => entry.Score).sort((a, b) => b.Score - a.Score);

        const processedEasyData = sortedEasyData.map((entry, index) => ({
          rank: index + 1,
          playerName: entry.Name, 
          score: entry.Score, 
        }));


        // Fetch normal data
        const normalResponse = await fetch('http://localhost:5000/normalleaderboard');
        const normalData = await normalResponse.json();

        // Convert to array and sort by score
        const normalArray = Object.values(normalData);
        const sortedDataNormal = normalArray.filter(entry => entry.Score).sort((a, b) => b.Score - a.Score);

        // Map array values
        const processedNormalData = sortedDataNormal.map((entry, index) => ({
          rank: index + 1,
          playerName: entry.Name, 
          score: entry.Score, 
        }));

        // Fetch hard data
        const hardResponse = await fetch('http://localhost:5000/hardleaderboard');
        const hardData = await hardResponse.json();

        // Convert to array and sort by score
        const hardArray = Object.values(hardData);
        const sortedDataHard = hardArray.filter(entry => entry.Score).sort((a, b) => b.Score - a.Score);

        // Map array values
        const processedHardData = sortedDataHard.map((entry, index) => ({
          rank: index + 1,
          playerName: entry.Name, 
          score: entry.Score, 
        }));
  
        setLeaderboardData({
          easy: processedEasyData,
          normal: processedNormalData,
          hard: processedHardData,
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

export default LeaderboardScreen;
