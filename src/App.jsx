/* eslint-disable no-unused-vars */
import { Login } from "./pages/Login"
import { Signup } from "./pages/Signup"
import { Routes } from 'react-router-dom';
import { Route ,Navigate} from 'react-router-dom';
import { Home } from "./pages/Homelyna";
import { BrowserRouter as Router } from 'react-router-dom';
import { AdminStatistics } from "./pages/AdminStatistics";
import { AdminProfil} from "./pages/AdminProfil";
import { AdminChangepw } from "./pages/AdminChangepw";
import { AdminUsers } from "./pages/AdminUsers";
import { AdminCoursesOnhold } from "./pages/AdminCoursesOnhold";
import { Courses } from "./pages/Courses";
import { Careers } from "./pages/Careers";
import { TermsAndConditions } from "./pages/terms&conditions";
import { CourseDetail } from "./pages/CourseDetail";
import { Courseaccept } from "./pages/courseaccept";
import { Coursedelete } from "./pages/Coursedelete";
import { MyLearning } from "./pages/MyLearning";
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
          <Route path="/Courses" element={<Courses/>}/>
          <Route path="/MyLearning" element={<MyLearning/>}/>         
          {/* < */}
          <Route path="/Careers" element={<Careers/>}/>
          <Route path="/termsandconditions" element={<TermsAndConditions/>}/>
          <Route path="admin/courseshold/course/:id" element={<CourseDetail/>}/>
          <Route path="admin/courseshold/course/:id/accept" element={<Courseaccept/>}/>
          <Route path="admin/courseshold/course/:id/delete" element={<Coursedelete/>}/>









          
        </Routes> 
         </div>
      </Router>
   )          
}

export default App


