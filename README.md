# TalentCampus UI

[![Open in GitPod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/from-referrer/)

This project uses **React** & **Vite** to create a fast and efficient development environment.

## Overview
This template provides a streamlined setup to get started with React using Vite, enabling features like Hot Module Replacement (HMR) and integrated ESLint rules for consistent code quality.

## Getting Started

To get up and running with the TalentCampus frontend, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd talentcampus-lms
   git checkout frontend
   ```

2. **Install Dependencies**
   Ensure you have [Node.js](https://nodejs.org/en/) installed, then run:
   ```bash
   npm install
   ```

3. **Running the Development Server**
   Start the development server with:
   ```bash
   npm run dev
   ```
   Your app should be available at `http://localhost:3000`.

## Configuration

### Plugins

This project uses the following official Vite plugins for React:

- **[@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md)**: This plugin utilizes [Babel](https://babeljs.io/) for enhanced Fast Refresh capabilities, allowing you to edit components in real-time without losing their state.

- **[@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc)**: An alternative plugin that employs [SWC](https://swc.rs/) for Fast Refresh. SWC is a Rust-based JavaScript/TypeScript compiler that provides faster performance for large projects.

### ESLint Configuration

To maintain a high standard of code quality, this project incorporates ESLint with predefined rules that help identify and fix common issues in your JavaScript and React code. Make sure to run ESLint regularly during development with:
```bash
npm run lint
```

## Additional Resources

- **Documentation**: For more information on React, visit the [official React reference](https://react.dev/reference/react)
- **Vite**: Learn more about Vite and its powerful features at the [Vite documentation](https://vitejs.dev/guide/).

## Contributing

Contributions to the TalentCampus are welcome! Feel free to send a PR or open an [issue](https://github.com/CorpoSense/talent-campus-lms/issues).

## License

This project is licensed under the MIT License.
