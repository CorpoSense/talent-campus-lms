import React from 'react';

export const Pagination = ({ currentPage, totalPages, onPageChange }) => {
  const handlePageClick = (page) => {
    if (page >= 1 && page <= totalPages) {
      onPageChange(page);
    }
  };

  return (
    <div className="flex justify-center items-center mt-4">
      <button
        className={`mx-1 px-3 py-1 rounded ${currentPage === 1 ? 'text-gray-300' : 'text-gray-600'}`}
        onClick={() => handlePageClick(currentPage - 1)}
        disabled={currentPage === 1}
      >
        &lt;
      </button>
      {[...Array(totalPages)].map((_, index) => (
        <button
          key={index}
          className={`mx-1 px-3 py-1 rounded border ${currentPage === index + 1 ? 'bg-blue-500 text-white' : 'text-gray-600'}`}
          onClick={() => handlePageClick(index + 1)}
        >
          {index + 1}
        </button>
      ))}
      <button
        className={`mx-1 px-3 py-1 rounded ${currentPage === totalPages ? 'text-gray-300' : 'text-gray-600'}`}
        onClick={() => handlePageClick(currentPage + 1)}
        disabled={currentPage === totalPages}
      >
        &gt;
      </button>
    </div>
  );
};
