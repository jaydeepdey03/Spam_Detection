import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [formData, setFormData] = useState({ sentence: '' })
  const [prediction, setPrediction] = useState(-1)

  const handleChange = (e) => {
    setFormData(prevState => {
      return { ...prevState, [e.target.name]: e.target.value }
    })
  }

  const fetchPrediction = async (e) => {
    e.preventDefault()
    // fetch prediction from axios
    const res = await axios({
      method: 'POST',
      url: 'http://localhost:5000/predict',
      data: formData
    });

    setPrediction(res.data.result)

  }

  return (
    <div className="p-20 h-screen flex flex-col">
      <h1 className='font-bold text-3xl text-center mb-7'>Spam Classifier</h1>
      <form action="">
        <textarea onChange={handleChange} name='sentence' value={formData.sentence} rows="10" className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none font-semibold">
        </textarea>
        <button onClick={fetchPrediction} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Check
        </button>
        {prediction === 0? <p className='font-semibold text-center text-2xl'>Not Spam</p>: <p className='font-semibold text-center text-2xl'>Spam</p>}
      </form>
    </div>
  )
}

export default App
