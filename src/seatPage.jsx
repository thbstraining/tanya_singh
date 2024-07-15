import Seat from "./components/Seat";
import ConcertHall from "./components/ConcertHall";
import ConcertDetails from "./components/ConcertDetails";
import SeatSelection from "./components/SeatSelection";

function seatFunc () {
    return (
        <div>
            <Seat/>
            <ConcertHall/>
            <ConcertDetails/>
            <SeatSelection/>
        </div>
    )
}

export default seatFunc;
