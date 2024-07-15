import  { useState, useEffect } from 'react';
import ConcertItem from './ConcertItem';
import "./ConcertList.css";

const ConcertList = () => {
  const [concerts, setConcerts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/concerts/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Concert data:', data);
        setConcerts(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching concerts:', error);
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h2>Available Concerts</h2>
      <div className='container'>
      {concerts.length === 0 ? (
        <div>No concerts available</div>
      ) : (
        concerts.map(concert => (
          <ConcertItem key={concert.id} concert={concert} />
        ))
      )}
      </div>
    </div>
  );
};

export default ConcertList;
