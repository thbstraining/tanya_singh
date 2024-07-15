/* eslint-disable react/prop-types */
import  { useState } from 'react';
import { Link } from 'react-router-dom';
import styles from './SeatSelection.module.css'; // Import CSS module

const SeatSelection = ({ concertId, availableSeats }) => {
  const [selectedSeats, setSelectedSeats] = useState([]);

  const handleSeatSelect = (seatNumber) => {
    setSelectedSeats([...selectedSeats, seatNumber]);
  };

  // const confirmReservation = () => {
  //   console.log('Selected seats:', selectedSeats);
  //   setSelectedSeats([]);
  // };

  return (
    <div className={styles.seatSelection}>
      <h2>Seat Selection</h2>
      <p>Available Seats: {availableSeats}</p>
      <p>Selected Seats: {selectedSeats.join(', ')}</p>
      <div className={styles.seatButtons}>
        {Array.from({ length: availableSeats }, (_, index) => (
          <button
            key={index}
            onClick={() => handleSeatSelect(index + 1)}
            disabled={selectedSeats.includes(index + 1)}
            className={styles.seatButton}
          >
            {index + 1}
          </button>
        ))}
      </div>
      <Link to={`/reservations/${concertId}`} className={styles.confirmButton}>
        Confirm Reservation
      </Link>
    </div>
  );
};

export default SeatSelection;
