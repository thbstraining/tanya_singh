
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import styles from './ConcertItem.module.css'; // Import CSS module

const ConcertItem = ({ concert }) => {
  if (!concert) {
    return <div>No more Concerts Available</div>;
  }

  return (
    <div className={styles.concertItem}>
      <h3>{concert.artist}</h3>
      <p>{concert.name}</p>
      <p>Date and Time: {concert.date}</p>
      <p>Available Seats: {concert.availableSeats}</p>
      <Link to={`/concerts/${concert.id}`} className={styles.viewSeatsButton}>
        View Seats
      </Link>
    </div>
  );
};

ConcertItem.propTypes = {
  concert: PropTypes.shape({
    artist: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    date: PropTypes.string.isRequired,
    availableSeats: PropTypes.number.isRequired,
    id: PropTypes.number.isRequired,
  }).isRequired,
};

export default ConcertItem;
