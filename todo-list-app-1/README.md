# To-do List App

This is a simple To-do List application built using HTML5, CSS3, and JavaScript, styled with Tailwind CSS in a pastel color theme. The app allows users to add and delete tasks, providing a clean and user-friendly interface.

## Project Structure

```
todo-list-app
├── src
│   ├── index.html      # Main HTML document for the To-do List app
│   ├── styles.css      # Custom styles utilizing Tailwind CSS
│   └── app.js          # JavaScript code for handling user interactions
├── tailwind.config.js   # Configuration file for Tailwind CSS
├── package.json         # npm configuration file
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd todo-list-app
   ```

2. **Install dependencies:**
   Make sure you have Node.js installed. Then run:
   ```bash
   npm install
   ```

3. **Build the project:**
   To compile the Tailwind CSS, run:
   ```bash
   npx tailwindcss -i ./src/styles.css -o ./dist/styles.css --watch
   ```

4. **Open the application:**
   Open `src/index.html` in your web browser to view the To-do List app.

## Usage

- Enter a task in the input field and click the "Add" button to add it to your list.
- Click the "Delete" button next to a task to remove it from the list.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is open-source and available under the [MIT License](LICENSE).