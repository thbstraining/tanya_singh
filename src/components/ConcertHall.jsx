
import PropTypes from 'prop-types';
import Seat from './Seat';
import styles from './ConcertHall.module.css'; // Import CSS module

const ConcertHall = ({ rows, cols, availableSeats, selectedSeats, onSelectSeat }) => {
  const seats = [];

  let seatNumber = 1;
  for (let row = 1; row <= rows; row++) {
    for (let col = 1; col <= cols; col++) {
      const isAvailable = availableSeats.includes(seatNumber);
      const isSelected = selectedSeats.includes(seatNumber);
      seats.push(
        <Seat
          key={seatNumber}
          number={seatNumber}
          isAvailable={isAvailable}
          isSelected={isSelected}
          onSelectSeat={onSelectSeat}
        />
      );
      seatNumber++;
    }
    seats.push(<br key={`br-${row}`} />);
  }

  return (
    <div className={styles.concertHall}>
      <h3>Seating Arrangement</h3>
      <div className={styles.seatsContainer}>
        {seats}
      </div>
    </div>
  );
};

ConcertHall.propTypes = {
  rows: PropTypes.number.isRequired,
  cols: PropTypes.number.isRequired,
  availableSeats: PropTypes.arrayOf(PropTypes.number).isRequired,
  selectedSeats: PropTypes.arrayOf(PropTypes.number).isRequired,
  onSelectSeat: PropTypes.func.isRequired,
};

export default ConcertHall;
