import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import './App.css';
import Register from './Register';
import Login from './login'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Register/>} />
        <Route path="/login" element={<Login/>} />
      </Routes>
    </Router>
  );
}

export default App;
