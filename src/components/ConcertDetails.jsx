import { useState } from 'react';
import ConcertHall from './ConcertHall';
import { useParams, useNavigate } from 'react-router-dom';
import styles from './ConcertDetails.module.css'; // Import CSS module

const ConcertDetails = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [selectedSeats, setSelectedSeats] = useState([]);
  const [confirmationMessage, setConfirmationMessage] = useState('');

  const handleSelectSeat = (seatNumber) => {
    if (selectedSeats.includes(seatNumber)) {
      setSelectedSeats(selectedSeats.filter(seat => seat !== seatNumber));
    } else {
      setSelectedSeats([...selectedSeats, seatNumber]);
    }
  };

  const handleConfirmReservation = () => {
    console.log('Selected Seats:', selectedSeats);
    setConfirmationMessage('Reservation confirmed for seats: ' + selectedSeats.join(', '));
    navigate(`/reservations/${id}`);
  };

  // Replace with actual API call to fetch concert data using id
  const concertData = {
    concertId: id,
    concertName: 'Example Concert',
    rows: 5,
    cols: 10,
    availableSeats: [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20],
  };

  return (
    <div className={styles.concertDetails}>
      <h2>{concertData.concertName}</h2>
      <ConcertHall
        rows={concertData.rows}
        cols={concertData.cols}
        availableSeats={concertData.availableSeats}
        selectedSeats={selectedSeats}
        onSelectSeat={handleSelectSeat}
      />
      <p>Selected Seats: {selectedSeats.join(', ')}</p>
      <button onClick={handleConfirmReservation} className={styles.confirmButton}>
        Confirm Reservation
      </button>
      {confirmationMessage && <p className={styles.confirmationMessage}>{confirmationMessage}</p>}
    </div>
  );
};

export default ConcertDetails;
