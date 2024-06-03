import React, {useState, useEffect} from 'react';
import axios from 'axios';

const api = axios.create({
    baseURL: 'https://backend-ialgzak72q-uc.a.run.app',
});

const Payments = () => {
    const [paymentData, setPaymentData] = useState({ amount: 0 });
    const [status, setStatus] = useState('');
    const [idTrack, setIdTrack] = useState(0); // Use state to track the ID

    useEffect(() => {
        const storedIdTrack = localStorage.getItem('idTrack');
        if (storedIdTrack) {
            setIdTrack(parseInt(storedIdTrack));
        }
    }, []);

    const handleChange = (e) => {
        setPaymentData({ ...paymentData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await api.post('/payments', {
                id: idTrack,
                amount: parseInt(paymentData.amount)
            });
            setStatus('Płatność się powiodła');
            setIdTrack(prevIdTrack => prevIdTrack + 1);
            localStorage.setItem('idTrack', idTrack + 1);
        } catch (error) {
            setStatus('Płatność się nie powiodła');
        }
    };

    return (
        <div>
            <h2>Formularz płatności</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Kwota:
                    <input type="number" name="amount" value={paymentData.amount} onChange={handleChange}/>
                </label>
                <button type="submit">Zapłać</button>
            </form>
            <p>Status: {status}</p>
        </div>
    );
};

export default Payments;
