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

  return (
    
    <><div className="min-h-[500px] w-[100%] font-['Lato']">
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

      <img src={course.imageb} alt={course.title} className="width: 100% h-90 mx-0 " />
      <div className="relative z-10 ml-10">
        <div className="mt-4">
          <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Category and duration </h1>
          <span className="font-semibold">{course.category}</span> | <span>{course.duration}</span>
        </div>
        <div className="mt-4">
          <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Course Overview </h1>
          <p className="leading-[0.01]">{course.overview}</p>
        </div>


        <div className="mt-4">
          <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Course Content </h1>
          <p className="leading-[0.01] font-bold mb-2">{course.modules.module1.title}</p>
          <p className="mb-4">{course.modules.module1.content}</p>
          <p className="leading-[0.01] font-bold mb-2">{course.modules.module2.title}</p>
          <p className="mb-4">{course.modules.module2.content}</p>
          <p className="leading-[0.01] font-bold mb-2">{course.modules.module3.title}</p>
          <p className="mb-4">{course.modules.module3.content}</p>
          <p className="leading-[0.01] font-bold mb-2">{course.modules.module4.title}</p>
          <p className="mb-4">{course.modules.module4.content}</p>
        </div>

        <div className="mt-4">
          <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Learning Outcomes </h1>
          <p className="mb-2">By the end of this course you will :</p>
          <p className="leading-[0.01]">{course.outcomes}</p>
        </div>

        <div className="mt-4 mb-20">
          <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Additional Notes </h1>
          <p className="leading-[0.01]">{course.notes}</p>
        </div>
         {/* Buttons */}
      <div className="space-x-4  mt-8 mb-10 -transform translate-x-80 flex items-center">
        <button className="bg-[#F2A5A5] text-red-500 px-10 py-2 rounded ">Delete</button>
        <button className="bg-[#20B486] text-white px-10 py-2 rounded">Accept</button>
      </div>

      </div>
    </div><Footer /></>
  );
};
