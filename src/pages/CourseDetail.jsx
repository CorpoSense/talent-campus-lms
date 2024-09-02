import React from 'react';
import { useParams } from 'react-router-dom';
import { sampleCourses } from '../data/data';
import { AdminNavbar } from '../components/AdminNavbar';
import { Footer } from '../components/Footerlyna';

export const CourseDetail = () => {
  const { id } = useParams();
  const course = sampleCourses.find(course => course.id === parseInt(id));

  if (!course) {
    return <div>Course not found</div>;
  }

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
      <div className="min-h-[500px] w-[100%] font-['Lato']">
        <AdminNavbar />
        <div className="relative bg-gradient-to-r from-[#202121] via-[#007BFF] via-[#F2F1E0] to-white py-12">
          {/* Transparent black rectangle */}
          <div className="absolute inset-0 bg-black opacity-70"></div>

          {/* Content */}
          <div className="relative z-10 ml-20">
            <h1 className="text-5xl font-bold text-white mt-10 mb-5">{course.title}</h1>
            <h6 className="text-white">{course.description}</h6>
          </div>
        </div>

        <img src={course.imageb} alt={course.title} className="w-full h-90 mx-0" />
        <div className="relative z-10 ml-10">
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

          {/* Buttons */}
          <div className="flex justify-end space-x-4 mr-8 mt-8 mb-10">
            <button className="bg-[#F2A5A5] text-red-500 px-10 py-2 rounded">Delete</button>
            <button className="bg-[#20B486] text-white px-10 py-2 rounded">Accept</button>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};
