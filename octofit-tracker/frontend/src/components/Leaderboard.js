
import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        setLeaderboard(Array.isArray(data) ? data : data.results || []);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <div className="card shadow mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4 text-primary">Leaderboard</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered align-middle">
            <thead className="table-primary">
              <tr>
                <th>#</th>
                <th>User</th>
                <th>Score</th>
                <th>Team</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.length === 0 ? (
                <tr><td colSpan="4" className="text-center">No leaderboard data.</td></tr>
              ) : (
                leaderboard.map((entry, idx) => (
                  <tr key={entry.id || idx}>
                    <td>{idx + 1}</td>
                    <td>{entry.user || '-'}</td>
                    <td>{entry.score || '-'}</td>
                    <td>{entry.team || '-'}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
