//App.js
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Register from './pages/Register';
import Login from './pages/login'
import Home from './pages/home';
import './App.css';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Register/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/home" element={<Home/>}></Route>
      </Routes>
    </Router>
  );
}

export default App;
