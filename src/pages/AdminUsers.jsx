import React, { useState } from 'react';
import { AdminNavbar } from '../components/AdminNavbar';
import { Pagination } from '../components/pagination';
import { ChevronDownIcon } from '@heroicons/react/24/solid'; // Add the icon package for the dropdown
import { Input } from "../components/Input";
import { basicschema } from "../schemas/index";
import profile from '../../public/profile.svg';
import logout from '../../public/logout.svg'; 
const initialStudents = [
    { id: 1, fname: 'Lyna', famname: 'KADRI', Email_Address: 'll_kadri@esi.dz' },
    { id: 2, fname: 'ikram', famname: 'KADRI', Email_Address: 'ik_kadri@esi.dz' },
    { id: 3, fname: 'Lyna', famname: 'KADRI', Email_Address: 'll_kadri@esi.dz' },
    { id: 4, fname: 'Lyna', famname: 'KADRI', Email_Address: 'll_kadri@esi.dz' },
    { id: 5, fname: 'Lyna', famname: 'KADRI', Email_Address: 'll_kadri@esi.dz' },
    { id: 6, fname: 'Lyna', famname: 'KADRI', Email_Address: 'll_kadri@esi.dz' },
    { id: 7, fname: 'Lyna', famname: 'KADRI', Email_Address: 'll_kadri@esi.dz' },
    { id: 8, fname: 'Lyna', famname: 'KADRI', Email_Address: 'll_kadri@esi.dz' },
    { id: 9, fname: 'Lyna', famname: 'KADRI', Email_Address: 'll_kadri@esi.dz' },
    { id: 10, fname: 'Lyna', famname: 'KADRI', Email_Address: 'll_kadri@esi.dz' },
    // More students...
  ];
  
  const initialInstructors = [
    { id: 1, fname: 'Ali', famname: 'BENZ', Courses: 'View', Email_Address: 'ali_benz@esi.dz' },
    { id: 2, fname: 'Sara', famname: 'RAB', Courses: 'View', Email_Address: 'sara_rab@esi.dz' },
    { id: 3, fname: 'Sara', famname: 'RAB', Courses: 'View', Email_Address: 'sara_rab@esi.dz' },
    { id: 4, fname: 'Sara', famname: 'RAB', Courses: 'View', Email_Address: 'sara_rab@esi.dz' },
    { id: 5, fname: 'Sara', famname: 'RAB', Courses: 'View', Email_Address: 'sara_rab@esi.dz' },
    { id: 6, fname: 'Sara', famname: 'RAB', Courses: 'View', Email_Address: 'sara_rab@esi.dz' },
    { id: 7, fname: 'Sara', famname: 'RAB', Courses: 'View', Email_Address: 'sara_rab@esi.dz' },
    { id: 8, fname: 'Sara', famname: 'RAB', Courses: 'View', Email_Address: 'sara_rab@esi.dz' },
    // More instructors...
  ];
  
  const itemsPerPage = 10;
  
  export const AdminUsers = () => {
    const [students, setStudents] = useState(initialStudents);
    const [instructors, setInstructors] = useState(initialInstructors);
    const [currentPage, setCurrentPage] = useState(1);
    const [activeSection, setActiveSection] = useState('Students');
    const [searchQuery, setSearchQuery] = useState('');
    const [filterOption, setFilterOption] = useState('fname');
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  
    const totalPages = Math.ceil(
      (activeSection === 'Students' ? students.length : instructors.length) /
      itemsPerPage
    );
  
    const handlePageChange = (page) => {
      setCurrentPage(page);
    };
  
    const handleDelete = (id) => {
      if (activeSection === 'Students') {
        setStudents(students.filter((student) => student.id !== id));
      } else if (activeSection === 'Instructors') {
        setInstructors(instructors.filter((instructor) => instructor.id !== id));
      }
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
  
    const filteredUsers =
      (activeSection === 'Students' ? students : instructors).filter(user =>
        user[filterOption].toLowerCase().includes(searchQuery.toLowerCase())
      );
  
    const currentUsers = filteredUsers.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);
  
    return (
      <>
        <AdminNavbar />
        <div className="min-h-[100vh] mx-auto w-[90%] mb-10">
          <h1 className="text-4xl tracking-wide font-bold mt-10 text-gradient">User Management</h1>
  
          {/* Search and Filter */}
          <div className="flex items-center mb-6 mt-8 space-x-4">
            <div className="relative w-full max-w-4xl"> {/* Adjust the max-w-4xl for a longer search bar */}
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
                      onClick={() => handleFilterChange('fname')}
                      className={`px-4 py-2 cursor-pointer ${filterOption === 'fname' ? 'bg-gray-100' : ''}`}
                    >
                      First Name
                    </li>
                    <li
                      onClick={() => handleFilterChange('famname')}
                      className={`px-4 py-2 cursor-pointer ${filterOption === 'famname' ? 'bg-gray-100' : ''}`}
                    >
                      Family Name
                    </li>
                    <li
                      onClick={() => handleFilterChange('Email_Address')}
                      className={`px-4 py-2 cursor-pointer ${filterOption === 'Email_Address' ? 'bg-gray-100' : ''}`}
                    >
                      Email Address
                    </li>
                  </ul>
                </div>
              )}
            </div>
          </div>
  
          {/* Navigation Links */}
          <div className="mt-8 mb-6">
            <ul className="flex space-x-8 text-lg">
              <li>
                <button
                  className={`focus:outline-none ${activeSection === 'Students' ? 'text-[#06A4FF] font-bold underline underline-offset-8' : 'text-gray-600'}`}
                  onClick={() => setActiveSection('Students')}
                >
                  Students
                </button>
              </li>
              <li>
                <button
                  className={`focus:outline-none ${activeSection === 'Instructors' ? 'text-[#06A4FF] font-bold underline underline-offset-8' : 'text-gray-600'}`}
                  onClick={() => setActiveSection('Instructors')}
                >
                  Instructors
                </button>
              </li>
            </ul>
          </div>
  
          {/* Users Table */}
          <div className="bg-white shadow-md rounded-lg p-6 flex flex-col h-[400px]">
            <h1 className="text-2xl mb-4">{activeSection}</h1>
            <div className="overflow-x-auto">
              <table className="min-w-full text-left bg-gray-50 border-separate border-spacing-0">
                <thead className="bg-[#F7FAFC] text-[#A0AEC0]">
                  <tr>
                    <th className="py-2 text-center border-b border-gray-200 font-bold">First Name</th>
                    <th className="py-2 text-center border-b border-gray-200 font-bold">Family Name</th>
                    <th className="py-2 text-center border-b border-gray-200 font-bold">Email Address</th>
                    {activeSection === 'Instructors' && (
                      <th className="py-2 text-center border-b border-gray-200 font-bold">Courses</th>
                    )}
                    <th className="py-2 text-center border-b border-gray-200 font-bold">Actions</th>
                  </tr>
                </thead>
                <tbody className="text-[#718096]">
                  {currentUsers.map((user, index) => (
                    <tr key={user.id} className={`border-b border-gray-200 ${index % 2 === 0 ? 'bg-gray-100' : 'bg-gray-50'}`}>
                      <td className="py-2 w-[150px] overflow-hidden whitespace-normal text-center">{user.fname}</td>
                      <td className="py-2 text-center">{user.famname}</td>
                      <td className="py-2 text-center">{user.Email_Address}</td>
                      {activeSection === 'Instructors' && (
                        <td className="py-2 text-center">
                          <span className="text-blue-500 cursor-pointer">View</span>
                        </td>
                      )}
                      <td
                        className="py-2 text-center text-red-500 cursor-pointer"
                        onClick={() => handleDelete(user.id)}
                      >
                        Delete
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            {/* Pagination Component */}
            <Pagination
              currentPage={currentPage}
              totalPages={totalPages}
              onPageChange={handlePageChange}
            />
          </div>
        </div>
      </>
    );
  };