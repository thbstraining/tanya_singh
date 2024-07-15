// App.js or wherever your routing is defined

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ConcertDetails from './components/ConcertDetails';
import SeatSelection from './components/SeatSelection';
import HomePage from './HomePage';
import ReservationPage from './ReservationPage'; // Import ReservationPage component

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/concerts/:id" element={<ConcertDetails />} />
        <Route path="/seats/:id" element={<SeatSelection />} />
        <Route path="/reservations/:id" element={<ReservationPage />} />
      </Routes>
    </Router>
  );
};

export default App;
