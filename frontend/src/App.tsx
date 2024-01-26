import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.scss";
import Home from "./pages/Home/Home.tsx";
import { ROUTES } from "./constants/routes.ts";
import GetVideo from "./pages/Home/GetVideo/GetVideo.tsx";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route 
                    path="/" 
                    element={<Home />} 
                />
                <Route 
                    path={ROUTES.GET_VIDEO}
                    element={<GetVideo />}
                />
                <Route
                    path="*"
                    element={<h1>404: Not Found</h1>}
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
