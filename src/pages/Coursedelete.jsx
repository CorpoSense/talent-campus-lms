import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { sampleCourses } from '../data/data';
import { AdminNavbar } from '../components/AdminNavbar';
import { Footer } from '../components/Footerlyna';
import x from "../../public/x.svg";

export const Coursedelete = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const course = sampleCourses.find(course => course.id === parseInt(id));

  if (!course) {
    return <div>Course not found</div>;
  }

  const handleNavigation = () => {
    navigate(`/admin/courseshold/course/${id}`);
  };

  const renderModuleContent = (module) => (
    <div key={module.title} className="mb-4">
      <p className="font-bold mb-2">{module.title}</p>
      <ul className="list-disc ml-5">
        {Object.values(module.content).map((content, index) => (
          <li className="mb-2" key={index}>{content}</li>
        ))}
      </ul>
    </div>
  );

  const renderOutcomes = (outcomes) => (
    <ul className="list-disc ml-5">
      {Object.values(outcomes).map((outcome, index) => (
        <li className="mb-2" key={index}>{outcome}</li>
      ))}
    </ul>
  );

  return (
    <> 
      <div className="min-h-[500px] w-[100%] font-['Lato'] relative">
        {/* Background Overlay */}
        <div className="absolute inset-0 bg-black opacity-70 h-[131%] z-10"></div>

        <AdminNavbar />

        {/* Main Content */}
        <div className="relative bg-gradient-to-r from-[#202121] via-[#007BFF] via-[#F2F1E0] to-white py-12">
          <div className="relative ml-20">
            <h1 className="text-5xl font-bold text-white mt-10 mb-5">{course.title}</h1>
            <h6 className="text-white">{course.description}</h6>
          </div>
        </div>

        <img src={course.imageb} alt={course.title} className="w-full h-90 mx-0 relative" />

        {/* White Container */}
        <div className="fixed inset-0 flex justify-center items-center z-30">
          <div className="bg-white shadow-md rounded-lg p-10 w-[50%] relative">
            <div className="absolute top-2 right-2">
              <button className="text-white px-1 py-1 rounded" onClick={handleNavigation}>
                <img src={x} className='w-[40px] h-[40px]' alt="Close" />
              </button>
            </div>
            <div>
              <h1 className="font-bold mb-10">Delete the course?</h1>
              <h1 className="mb-10">Are you sure you want to delete the course?</h1>
            </div>
            <div className="flex justify-end space-x-4 mb-2">
              <button className="bg-[#EFEFEF] text-black px-10 py-2 rounded" onClick={handleNavigation}>Cancel</button>
              <button className="bg-red-500 text-white px-10 py-2 rounded" onClick={handleNavigation}>Yes</button>
            </div>
          </div>
        </div>

        <div className="relative z-20 ml-10">
          <div className="mt-4">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Category and duration</h1>
            <span className="font-semibold">{course.category}</span> | <span>{course.duration}</span>
          </div>
          <div className="mt-4">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Course Overview</h1>
            <p className="leading-[0.01]">{course.overview}</p>
          </div>
          <div className="mt-4">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Course Content</h1>
            {Object.values(course.modules).map(module => renderModuleContent(module))}
          </div>
          <div className="mt-4">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Learning Outcomes</h1>
            <p className="mb-4">By the end of this course you will:</p>
            {Object.values(course.modules).map(module => renderOutcomes(module.outcomes))}
          </div>
          <div className="mt-4 mb-20">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Additional Notes</h1>
            <p className="leading-[0.01]">{course.notes}</p>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};
