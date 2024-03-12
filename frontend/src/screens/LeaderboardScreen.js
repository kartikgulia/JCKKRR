import React, { useState, useEffect } from "react";
import "../styles/LeaderboardScreen.css";
import { Link } from "react-router-dom";
import SERVER_URL from "../config";
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
    medium: [],
    hard: [],
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLeaderboardData = async () => {
      try {
        // Fetch data from your Firestore database for Easy difficulty
        const easyResponse = await fetch(`${SERVER_URL}/easyLeaderboard`);
        const easyData = await easyResponse.json();

        // Convert to array and sort by score
        const easyArray = Object.values(easyData);
        const sortedEasyData = easyArray
          .filter((entry) => entry.Score)
          .sort((a, b) => b.Score - a.Score);

        const processedEasyData = sortedEasyData.map((entry, index) => ({
          rank: index + 1,
          playerName: entry.Name,
          score: entry.Score,
        }));

        // Fetch medium data
        const mediumResponse = await fetch(`${SERVER_URL}/mediumleaderboard`);
        const mediumData = await mediumResponse.json();

        // Convert to array and sort by score
        const mediumArray = Object.values(mediumData);
        const sortedDataMedium = mediumArray
          .filter((entry) => entry.Score)
          .sort((a, b) => b.Score - a.Score);

        // Map array values
        const processedMediumData = sortedDataMedium.map((entry, index) => ({
          rank: index + 1,
          playerName: entry.Name,
          score: entry.Score,
        }));

        // Fetch hard data
        const hardResponse = await fetch(`${SERVER_URL}/hardLeaderboard`);
        const hardData = await hardResponse.json();

        // Convert to array and sort by score
        const hardArray = Object.values(hardData);
        const sortedDataHard = hardArray
          .filter((entry) => entry.Score)
          .sort((a, b) => b.Score - a.Score);

        // Map array values
        const processedHardData = sortedDataHard.map((entry, index) => ({
          rank: index + 1,
          playerName: entry.Name,
          score: entry.Score,
        }));

        setLeaderboardData({
          easy: processedEasyData,
          medium: processedMediumData,
          hard: processedHardData,
        });

        setLoading(false);
      } catch (error) {
        console.error("Error fetching leaderboard data:", error);
        setLoading(false);
      }
    };

    fetchLeaderboardData();
  }, []);

  return (
    <div className="leaderboard-screen">
      <Link to="/gameSelect" className="back-button">
        Back
      </Link>
      <h1 className="leaderboard-title">Leaderboard</h1>
      {loading ? (
        <p>Loading leaderboard...</p>
      ) : (
        <div className="leaderboards-wrapper">
          <LeaderboardTable data={leaderboardData.easy} difficulty="Easy" />
          <LeaderboardTable data={leaderboardData.medium} difficulty="Medium" />
          <LeaderboardTable data={leaderboardData.hard} difficulty="Hard" />
        </div>
      )}
    </div>
  );
};

export default LeaderboardScreen;
