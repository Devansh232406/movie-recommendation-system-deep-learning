import { useEffect, useState } from "react";
import axios from "axios";
import "./index.css";

function MovieCard({ movie, index }) {
  return (
    <div className="movie-card">
      <img
        src={`https://picsum.photos/300/450?random=${index + 20}`}
        alt={movie.title}
      />

      <div className="movie-info">
        <h3>{movie.title}</h3>
        <span>⭐ {movie.predicted_rating}</span>
      </div>
    </div>
  );
}

function App() {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const userId = 1;

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/recommendations/${userId}`)
      .then((response) => {
        console.log("API:", response.data);
        setMovies(response.data.recommendations);
      })
      .catch((err) => {
        console.error(err);
        setError("Could not load recommendations.");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div className="app">

      {/* NAVBAR */}
      <nav className="navbar">
        <div className="logo">
          CINE<span>AI</span>
        </div>

        <div className="nav-links">
          <a className="active">Home</a>
          <a>Movies</a>
          <a>My List</a>
        </div>

        <div className="profile">👤</div>
      </nav>


      {/* HERO */}
      <section className="hero">

        <img
          src="https://picsum.photos/1600/900?random=100"
          className="hero-image"
          alt="Featured movie"
        />

        <div className="hero-overlay"></div>

        <div className="hero-content">

          <p className="ai-label">AI RECOMMENDED</p>

          <h1>Discover Your Next Favorite</h1>

          <p>
            Personalized movie recommendations powered by
            Neural Collaborative Filtering.
          </p>

          <button>▶ Explore Movies</button>

        </div>

      </section>


      {/* CONTENT */}
      <main className="content">

        <div className="section-header">
          <h2>Recommended For You</h2>
          <p>Personalized by your NCF model</p>
        </div>

        {loading && (
          <div className="loading">
            🧠 AI is generating your recommendations...
          </div>
        )}

        {error && (
          <div className="error">
            ❌ {error}
            <br />
            <small>
              Make sure FastAPI is running on port 8000.
            </small>
          </div>
        )}

        {!loading && !error && (
          <div className="movie-row">
            {movies.map((movie, index) => (
              <MovieCard
                key={movie.movie_id}
                movie={movie}
                index={index}
              />
            ))}
          </div>
        )}

      </main>

    </div>
  );
}

export default App;