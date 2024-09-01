/* eslint-disable no-unused-vars */
import { Navbar } from "./components/Navbar"
import { AdminNavbar } from "./components/AdminNavbar";
import { Login } from "./pages/Login"
import { Signup } from "./pages/Signup"
import { Routes } from 'react-router-dom';
import { Hero } from "./components/Hero";
import { Route ,Navigate} from 'react-router-dom';
import { Home } from "./pages/Home";
import { BrowserRouter as Router } from 'react-router-dom';
import { AdminStatistics } from "./pages/AdminStatistics";
import { AdminProfil} from "./pages/AdminProfil";
import { AdminChangepw } from "./pages/AdminChangepw";
import { AdminUsers } from "./pages/AdminUsers";
import { AdminCoursesOnhold } from "./pages/AdminCoursesOnhold";
import { privacyPolicy } from "./pages/privacyPolicy";
import { Careers } from "./pages/Carrers";


function App() {
  
 
  return (
    // bg-gradient-to-br from-transparent from-40% via-[#88baf0]/60 bg-opacity-15 to-[#fde18d]/60
      <Router>
          <div className=" min-h-screen  bg-[#f8f9fa] ">
        <Routes>
          <Route path="/Login" element={<Login/>}/>
          <Route path="/Signup" element={<Signup/>}/>
          <Route path="/" element={<Home/>}/>
          <Route path="/admin" element={<AdminStatistics/>}/>
          <Route path="/admin/profil" element={<AdminProfil/>}/>
          <Route path="/admin/changepassword" element={<AdminChangepw/>}/>
          <Route path="/admin/users" element={<AdminUsers/>}/>
          <Route path="/admin/courseshold" element={<AdminCoursesOnhold/>}/>
          <Route path="/Careers" element={<Careers/>}/>
          <Route path="/privacyPolicy" element={<privacyPolicy/>}/>

        </Routes> 
         </div>
      </Router>
   )          
}

export default App


