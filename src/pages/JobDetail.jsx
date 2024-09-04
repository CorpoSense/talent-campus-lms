import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { sampleJobs } from '../data/data';
import { AdminNavbar } from '../components/AdminNavbar';
import { Footer } from '../components/Footerlyna';

export const JobDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const job = sampleJobs.find(job => job.id === parseInt(id));

  if (!job) {
    return <div>Job not found</div>;
  }

  const handleDeleteClick = () => {
    navigate(`/admin/jobs/job/${id}/delete`);
  };

  const handleAcceptClick = () => {
    navigate(`/admin/jobs/job/${id}/accept`);
  };

  const renderKeyResponsibilities = (responsibilities) => (
    <ul className="list-disc ml-5">
      {Object.values(responsibilities).map((resp, index) => (
        <li className="mb-2" key={index}>{resp}</li>
      ))}
    </ul>
  );

  const renderRequiredSkills = (skills) => (
    <ul className="list-disc ml-5">
      {Object.values(skills).map((skill, index) => (
        <li className="mb-2" key={index}>{skill}</li>
      ))}
    </ul>
  );

  const renderBenefits = (benefits) => (
    <ul className="list-disc ml-5">
      {Object.values(benefits).map((benefit, index) => (
        <li className="mb-2" key={index}>{benefit}</li>
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
            <h1 className="text-5xl font-bold text-white mt-10 mb-5">{job.title}</h1>
            <h6 className="text-white">{job.description}</h6>
          </div>
          
          
          <img 
            src={job.image} 
            alt={job.title} 
            className="w-1/4 h-auto object-cover absolute top-20 right-10 z-20" // Adjust width and positioning
          />
        </div>

        <div className="relative z-10 ml-10">
          <div className="mt-4">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Category and Location</h1>
            <span className="font-semibold">{job.category}</span> | <span>{job.location}</span>
          </div>
          <div className="mt-4">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Key Responsibilities</h1>
            {renderKeyResponsibilities(job.keyResponsibilities)}
          </div>

          <div className="mt-4">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Required Skills and Qualifications</h1>
            {renderRequiredSkills(job.requiredSkillsAndQualifications)}
          </div>

          <div className="mt-4">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">Benefits</h1>
            {renderBenefits(job.benefits)}
          </div>

          <div className="mt-4 mb-20">
            <h1 className="text-2xl tracking-wide font-bold mt-10 text-gradient mb-4">How to Apply</h1>
            <p className="leading-[0.01]">{job.howToApply}</p>
          </div>

          {/* Buttons */}
          <div className="flex justify-end space-x-4 mr-8 mt-8 mb-10">
            <button 
              className="bg-[#F2A5A5] text-red-500 px-10 py-2 rounded"
              onClick={handleDeleteClick}
            >
              Delete
            </button>
            <button 
              className="bg-[#20B486] text-white px-10 py-2 rounded"
              onClick={handleAcceptClick}
            >
              Accept
            </button>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};
