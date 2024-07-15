/* eslint-disable no-unused-vars */
import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import styles from './Reserve.module.css';

const SeatSelection = ({ concertId, availableSeats }) => {
  const [reservations, setReservations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/reservations/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Reservations:', data);
        setReservations(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching reservations:', error);
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className={styles.loadingMessage}>Loading reservations...</div>;
  }

  if (error) {
    return <div className={styles.errorMessage}>Error fetching reservations: {error.message}</div>;
  }

  return (
    <div className={styles.reservationsContainer}>
      <h3>Current Reservations</h3>
      <ul className={styles.reservationsList}>
        {reservations.length === 0 ? (
          <li className={styles.reservationItem}>No reservations found.</li>
        ) : (
          reservations.map(reservation => (
            <li key={reservation.id} className={styles.reservationItem}>
              <p>Name: {reservation.name}</p>
              <p>Email: {reservation.email}</p>
              <p>Concert: {reservation.concert}</p>
              <p>Seating Layout: {reservation.seating_layout}</p>
            </li>
          ))
        )}
      </ul>
    </div>
  );
};

SeatSelection.propTypes = {
  concertId: PropTypes.number.isRequired,
  availableSeats: PropTypes.number.isRequired,
};

export default SeatSelection;
