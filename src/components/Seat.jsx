
import PropTypes from 'prop-types';
import styles from './Seat.module.css'; // Import CSS module

const Seat = ({ number, isAvailable, isSelected, onSelectSeat }) => {
  const seatStyle = {
    backgroundColor: isSelected ? '#007bff' : (isAvailable ? '#28a745' : '#dc3545'),
    width: '40px',
    height: '40px',
    margin: '5px',
    cursor: isAvailable ? 'pointer' : 'not-allowed',
  };

  const handleClick = () => {
    if (isAvailable) {
      onSelectSeat(number);
    }
  };

  return (
    <div
      style={seatStyle}
      className={styles.seat}
      onClick={handleClick}
    >
      {number}
    </div>
  );
};

Seat.propTypes = {
  number: PropTypes.number.isRequired,
  isAvailable: PropTypes.bool.isRequired,
  isSelected: PropTypes.bool.isRequired,
  onSelectSeat: PropTypes.func.isRequired,
};

export default Seat;
