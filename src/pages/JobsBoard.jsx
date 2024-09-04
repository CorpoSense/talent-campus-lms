import React, { useState } from 'react';
import { AdminNavbar } from '../components/AdminNavbar';
import { Pagination } from '../components/pagination';
import { ChevronDownIcon } from '@heroicons/react/24/solid';
import { Link } from 'react-router-dom';
import { sampleJobs } from '../data/data';
import location from "/location.svg";
import timer from "/timer.svg";
import { Footer } from '../components/Footerlyna';

// Initialize jobs data
const initialJobs = sampleJobs;

const categories = {
  Design: initialJobs.filter(job => job.category === 'Design').slice(0, 12),
  Development: initialJobs.filter(job => job.category === 'Development').slice(0, 12),
  Marketing: initialJobs.filter(job => job.category === 'Marketing').slice(0, 12),
  Business: initialJobs.filter(job => job.category === 'Business').slice(0, 12),
  AllCategories: initialJobs.slice(0, 48),
};

const itemsPerPage = 5;

export const JobsOnhold = () => {
  const [jobsOnHold, setJobsOnHold] = useState(categories.AllCategories);
  const [currentPage, setCurrentPage] = useState(1);
  const [activeCategory, setActiveCategory] = useState('AllCategories');
  const [searchQuery, setSearchQuery] = useState('');
  const [filterOption, setFilterOption] = useState('title');
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const getJobs = () => categories[activeCategory] || [];
  const totalPages = Math.ceil(getJobs().length / itemsPerPage);

  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  const handleSearch = (e) => {
    setSearchQuery(e.target.value);
  };

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  const handleFilterChange = (option) => {
    setFilterOption(option);
    setIsDropdownOpen(false);
  };

  const handleDelete = (id) => {
    setJobsOnHold(jobsOnHold.filter((job) => job.id !== id));
  };

  const filteredJobs = getJobs().filter(job =>
    job[filterOption]?.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const currentJobs = filteredJobs.slice(startIndex, endIndex);

  return (
    <>
      <AdminNavbar />
      <div className="min-h-[100vh] mx-auto w-[90%] mb-10 font-lato">
        <h1 className="text-4xl tracking-wide font-bold mt-10 text-gradient">Jobs Board</h1>

        {/* Category Navigation */}
        <div className="flex items-center justify-between mb-6 mt-8 space-x-4">
          <ul className="flex space-x-8 text-lg">
            {Object.keys(categories).map(category => (
              <li key={category}>
                <button
                  className={`focus:outline-none ${activeCategory === category ? 'text-[#20B486] font-bold underline underline-offset-8' : 'text-gray-600'}`}
                  onClick={() => {
                    setActiveCategory(category);
                    setJobsOnHold(categories[category] || []);
                    setCurrentPage(1); // Reset to first page when category changes
                  }}
                >
                  {category}
                </button>
              </li>
            ))}
          </ul>

          {/* Search and Filter */}
          <div className="relative w-full max-w-4xl">
            <input
              type="text"
              placeholder="Search..."
              value={searchQuery}
              onChange={handleSearch}
              className="border border-gray-300 rounded-md p-2 w-full"
            />
            <button
              onClick={toggleDropdown}
              className="absolute right-2 top-1/2 transform -translate-y-1/2"
            >
              <ChevronDownIcon className="w-5 h-5 text-gray-500" />
            </button>
            {isDropdownOpen && (
              <div className="absolute right-0 mt-2 bg-white border border-gray-300 rounded-md shadow-lg">
                <ul>
                  <li
                    onClick={() => handleFilterChange('title')}
                    className={`px-4 py-2 cursor-pointer ${filterOption === 'title' ? 'bg-gray-100' : ''}`}
                  >
                    Title
                  </li>
                </ul>
              </div>
            )}
          </div>
        </div>

        {/* Jobs List */}
        <div className="bg-white shadow-md rounded-lg p-6">
          <h1 className="text-2xl mb-4">{activeCategory}</h1>
          <div className="space-y-6">
            {currentJobs.map((job) => (
              <div key={job.id} className="flex items-center justify-between p-4 rounded-lg bg-white shadow-lg mb-4">
                <Link to={`./job/${job.id}`} className="w-full flex">
                  <img
                    src={job.image}
                    alt={job.title}
                    className="w-1/4 h-40 object-cover rounded-lg"
                  />
                  <div className="flex flex-col justify-between w-3/4 ml-4">
                    <div>
                      <h2 className="font-bold text-xl">{job.title}</h2>
                      <p className="text-gray-500 mt-2">{job.description}</p>
                    </div>
                    <div className="flex justify-between items-center mt-4">
                      <div className="flex space-x-4">
                        <span className="font-semibold text-[#268FFF] flex space-x-4">
                          <img src={location} alt="location" />
                          {job.location}
                        </span>
                        <span className="font-semibold text-[#268FFF] ml-4 flex space-x-4">
                          <img src={timer} alt="timer" />
                          {job.datePosted}
                        </span>
                      </div>
                      <div className="flex space-x-4">
                        <button className="text-blue-500 px-4 py-2 rounded">Edit</button>
                        <button
                          className="text-red-500 px-4 py-2 rounded cursor-pointer"
                          onClick={(e) => {
                            e.stopPropagation(); // Prevents the click event from bubbling up to the Link
                            handleDelete(job.id);
                          }}
                        >
                          Remove
                        </button>
                      </div>
                    </div>
                  </div>
                </Link>
              </div>
            ))}
          </div>
          <Pagination
            currentPage={currentPage}
            totalPages={totalPages}
            onPageChange={handlePageChange}
          />
        </div>
        
      </div>
      <Footer />
    </>
  );
};
