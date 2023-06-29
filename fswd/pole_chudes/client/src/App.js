import './App.css';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Register from './pages/register';
import Login from './pages/login';
import Game from './pages/game';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Register/>} />
        <Route path="/login" element={<Login/>}/>
        <Route path="/game" element={<Game/>}/>
      </Routes>
    </Router>
  );
}

export default App;
