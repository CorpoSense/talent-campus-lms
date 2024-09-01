import React, { useState } from 'react';
import { AdminNavbar } from '../components/AdminNavbar';
import { Pagination } from '../components/pagination';
import { ChevronDownIcon } from '@heroicons/react/24/solid';
import { Link } from 'react-router-dom';
import { Footer } from '../components/footer';

// Sample course data for each category
const sampleCourses = [
    {
      image: "../public/course.png",
      category: 'Design',
      duration: '3h 45m',
      title: 'Course Title 1',
      description: 'Short description of the course.',
    },
    {
      image: "../public/course.png",
      category: 'Development',
      duration: '4h 30m',
      title: 'Course Title 2',
      description: 'Short description of the course.',
    },
    {
      image: "../public/course.png",
      category: 'Design',
      duration: '4h 30m',
      title: 'Course Title 3',
      description: 'Short description of the course.',
    },{
      image: "../public/course.png",
      category: 'Development',
      duration: '4h 30m',
      title: 'Course Title 4',
      description: 'Short description of the course.',
    },{
      image: "../public/course.png",
      category: 'Design',
      duration: '4h 30m',
      title: 'Course Title 5',
      description: 'Short description of the course.',
    },{
      image: "../public/course.png",
      category: 'Design',
      duration: '4h 30m',
      title: 'Course Title 6',
      description: 'Short description of the course.',
    },{
      image: "../public/course.png",
      category: 'Marketing',
      duration: '4h 00m',
      title: 'Course Title 7',
      description: 'Short description of the course.',
    },{
      image: "../public/course.png",
      category: 'Marketing',
      duration: '3h 30m',
      title: 'Course Title 8',
      description: 'Short description of the course.',
    },{
      image: "../public/course.png",
      category: 'Business',
      duration: '2h 30m',
      title: 'Course Title 9',
      description: 'Short description of the course.',
    },{
      image: "../public/course.png",
      category: 'Business',
      duration: '3h 30m',
      title: 'Course Title 10',
      description: 'Short description of the course.',
    },{
      image: "../public/course.png",
      category: 'Marketing',
      duration: '4h 30m',
      title: 'Course Title 11',
      description: 'Short description of the course.',
    },{
      image: "../public/course.png",
      category: 'Development',
      duration: '4h 30m',
      title: 'Course Title 12',
      description: 'Short description of the course.',
    },
    {
        image: "../public/course.png",
        category: 'Development',
        duration: '4h 30m',
        title: 'Course Title 13',
        description: 'Short description of the course.',
      },
      {
        image: "../public/course.png",
        category: 'Development',
        duration: '4h 30m',
        title: 'Course Title 14',
        description: 'Short description of the course.',
      },
    // Add more courses as needed
  ];

  const categories = {
    Design: sampleCourses.filter(course => course.category === 'Design').slice(0, 12),
    Development: sampleCourses.filter(course => course.category === 'Development').slice(0, 12),
    Marketing: sampleCourses.filter(course => course.category === 'Marketing').slice(0, 12),
    Business: sampleCourses.filter(course => course.category === 'Business').slice(0, 12),
    AllCategories: sampleCourses.slice(0, 48),
  };
  
  const itemsPerPage = 9;
  
  export const AdminCoursesOnhold = () => {
    const [currentPage, setCurrentPage] = useState(1);
    const [activeCategory, setActiveCategory] = useState('AllCategories');
    const [searchQuery, setSearchQuery] = useState('');
    const [filterOption, setFilterOption] = useState('title');
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  
    const getCourses = () => categories[activeCategory] || [];
    const totalPages = Math.ceil(getCourses().length / itemsPerPage);
  
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
  
    const filteredCourses = getCourses().filter(course =>
      course[filterOption]?.toLowerCase().includes(searchQuery.toLowerCase())
    );
  
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const currentCourses = filteredCourses.slice(startIndex, endIndex);
  
    return (
      <>
      
        <AdminNavbar />
        <div className="min-h-[100vh] mx-auto w-[90%] mb-10 font-lato">
          <h1 className="text-4xl tracking-wide font-bold mt-10 text-gradient">Course Management</h1>
  
          <div className="flex items-center justify-between mb-6 mt-8 space-x-4">
            <ul className="flex space-x-8 text-lg">
              {Object.keys(categories).map(category => (
                <li key={category}>
                  <button
                    className={`focus:outline-none ${activeCategory === category ? 'text-[#06A4FF] font-bold underline underline-offset-8' : 'text-gray-600'}`}
                    onClick={() => setActiveCategory(category)}
                  >
                    {category}
                  </button>
                </li>
              ))}
            </ul>
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
  
          <div className="bg-white shadow-md rounded-lg p-6">
            <h1 className="text-2xl mb-4">{activeCategory}</h1>
            <div className="grid grid-cols-3 gap-6"> {/* Updated gap for space between containers */}
              {currentCourses.map((course, index) => (
                <Link to={`/course/${index}`} key={index}>
                  <div className="cursor-pointer shadow-lg p-4 rounded-lg bg-white"> {/* Added shadow */}
                    <img src={course.image} alt={course.title} className="w-full h-40 object-cover rounded-lg" />
                    <div className="flex justify-between items-center mt-4">
                      <span className="font-semibold">{course.category}</span>
                      <span className="text-gray-500">{course.duration}</span>
                    </div>
                    <h2 className="mt-4 font-bold">{course.title}</h2>
                    <p className="text-gray-500 mt-2">{course.description}</p> {/* Lighter text for description */}
                    <button className="bg-yellow-500 text-white px-4 py-2 mt-4 rounded">On Hold</button>
                  </div>
                </Link>
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