# Live Timing Dash | FAll 2023
Serena Duncan (smd334)
# Summary
## System Description
The Live Timing Dash is a ReactJS-based platform that displays information about the vehicle's performance as it runs. This dashboard is used by team members during competition to see how the car is performing and gather live data about it's performance. It is intended to provide a bridge between the driver and the rest of the team by ensuring the team is able to moniter the car during drives and ensure it is performing properly. 

The dashboard currently contains a timer that team members can operate to track the car's runs. Additionally, it displays statistics about the power, speed, voltage consumed, and other information fetched from the DAQ. In the future, the dashboard will contain live updating graphs that will allow team members to track these values over time. 

The frontend of the dashboard is built in Typescript with the React framework, which uses HTML/TSX/CSS. The dashboard maintains connections with the mobile dashboard and historical dashboard through Websockets.

![A screencap of the live timing dash, December 2023](src/assets/dash.png)

## Terminology
**Server** : A piece of software that provides resources (such as data) on demand to the client. Handles client requests. <br>
**Client** : The user, the one making a request of the server. <br>
**Frontend** : The part of the website the user can view and interact with. <br>
**Backend** : The "behind-the-scenes" part of the website that handles fetching data and maintaining a connection with the server. <br>
**DAQ (Data Auisition system)** : A piece of hardware that collects data about the vehicle and sends it to the server. <br>
**Mobile Dash** : Hosted on a phone that the driver of our vehicle carries with them. Displays up-to-date information about the car and posts this information to the live timing dash. <br>
**React TS** : A Typescript based library that provides functionality for building front-end interfaces. <br>
**Components** : The building blocks of React webpages; display an element on the screen and can provide interactivity. <br>
**Typescript** : A type-safe version of Javascript. <br>
**HTML** : Stands for Hyper-Text Markup Language. The base language used to specify the layout of webpages. <br>
**CSS** : Stands for Cascading Style Sheets. A language that provides a way to specify the look of webpages. <br>
**TSX** : Allows the programmer to create HTML elements in Typescript. These elements can than be displayed in React components. <br>
**Vite** : A tool that helps make development of front end projects easier. <br>
**useEffect** : React's useEffect hook allows the user to run a piece of setup code  each time one of the specified variables (called dependcies, often connected to external systems, such as the server) changes. It runs a piece of setup code when the component is first loaded onto the page. After a dependency changes, a piece of cleanup code is run before the setup code reruns. <br>
**useState** : Creates a variable and a function to update its value. <br>

# How To Use
Steps:
1) [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2) Install [Node.js](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs) version 18+.20+
3) Navigate to main directory (LiveTimingDashTS2023)
4) Run `npm install` in terminal
5) In the terminal, run `npm start` to view site (or `npm run dev` to view developmental version)!

# Detailed System Description
## Application Architecture: Frontend
### Overview
The frontend for the live timing dash was built with React TS, which integrates TSX, CSS, and HTML to build interactive web pages. The project was built with [Vite](https://vitejs.dev/guide/). The code is split up into a variety of different files. index.html provides the webpage container for the components, which are housed in the various component files and displayed in App.tsx, which in turn is displayed in    main.tsx. The .css files contain the styles used for text and colors on the dashboard. The other files contain the Websocket connection (explained the Backend section of this README) and other files necessary for creating and displaying the webpage (more information [here](https://vitejs.dev/guide/#scaffolding-your-first-vite-project))

### index.html
Provides the layout for the webpage and displays the React components.

### main.tsx
Entry point to display the App.tsx file.

### App.tsx
The App.tsx file is the primary component and acts as a container for all the other components in this project. Components are rendered in App.tsx with 
`<NameHere props\>`. 

### Component Files
The component files are the .tsx files in the src folder (excluding main.tsx, App.tsx, Socketprovider.tsx, and useSocket.tsx). These components split the interface into small, reusable blocks that each contain or handle one primary task. These components handle state changes due to data updating and display useful information about the car. Components all contain a few key elements:
1) Interface for a Data object <br>
This interface provides a basic layout for a data object that contains the information the component is tasked with displaying. The object is created within the component and updated periodically as new data comes in from the server.
2) Websocket Connection via useEffect hook <br>
Each component uses a useEffect hook to update its data object with new data from the server. 
3) a return() function <br>
The return function contains the TSX elements the component will display on the webpage.
4) variables for displaying data <br>
Variables are created with the useState hook and updated within the useEffect hook when new data needs to be displayed.

## Application Architecture: Backend
The backend allows the live dashboard to maintain a constant connection to the server, through which the dash can recieve updated information from the DAQ.

### Server.ts
This file will set up the connection between the dashboard and the mobile dash, which will send over updated data from the DAQ.

### Websockets
This project utilizes the Websockets library to handle server connections. The socket is opened when the webpage starts up, and stays opne until the page closes. If the connection drops, the socket reconnects, as the dashboard always needs to maintain the connection in order to display the most up to date data. 

The endpoint for this connection has been temporarily set to a dummy endpoint that points back to the server the frontend is hosted on. Once the mobile dash and DAQ are completed, the endpoint will be set to the Mobile Dash backend. The Websocket connection is set up in SocketProvider.tsx, which ties the Websocket object to a global variable. In useSocket.tsx, this variable is turned into a React Hook that enables the programmer to quickly and easily call the socket connection anywhere it may be needed. The SocketProvider wraps all other elements in App.tsx, meaning the server only maintains one socket that is then called in all other components as needed.

# Challenges
One of the biggest challenges with this project was having to teach myself about TypeScript and WebSockets. Typescript was fairly easy to pick up, but porting the code over ended up being very difficult due to the original code not being type safe and containing many issues with how the server connection was handled. Websockets was also a bit difficult to understand, as they were handled improperly in the old codebase and I had to figure out the proper way of setting it up. I ended up creating a useSocket() hook that allowed me to call the WebSocket connection in an easy to read way.

The other challenge of the project was working with the old codebase. The previous dash uses out of date React practices old database code is not well documented and very difficult to comb through, so even tasks as simple as simply seeing what information I needed to include turned into a fairly long process. I ended up deciding to do a full rewrite of the dashboard, as much of the old codebase was unusable.

# Testing

# Semester Work
