import './App.css';
import Home from './components/Home';
import Lifting from './components/Lifting';
import Skating from './components/Skating';
import Tennis from './components/Tennis';
import Archery from './components/Archery';
import Volleyball from './components/Volleyball';
import Curls from './components/Curls';
import Squats from './components/Squats';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/lifting" element={<Lifting />} />
          <Route path="/skating" element={<Skating />} />
          <Route path="/tennis" element={<Tennis />} />
          <Route path="/archery" element={<Archery/>} />
          <Route path="/volleyball" element={<Volleyball/>} />
          <Route path="/lifting/curls" element={<Curls/>} />
          <Route path="/lifting/squats" element={<Squats/>} />

    </Routes>
  );
}

export default App;
