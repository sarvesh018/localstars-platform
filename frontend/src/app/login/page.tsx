"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import api from "@/lib/api";

export default function LoginPage() {

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const router = useRouter();

  const loginUser = async () => {
    setLoading(true);
    try {

      const formData = new URLSearchParams();
      
      formData.append("username", email);

      formData.append("password", password);

      const response = await api.post(
        "/auth/login",
        formData,
        {
          headers: {
            "Content-Type":
              "application/x-www-form-urlencoded",
          },
        }
      );

      localStorage.setItem(
        "token",
        response.data.access_token
      );

      setMessage("Login successful");
      router.push("/dashboard");

    } catch (error: any) {

      setMessage(
        error.response?.data?.detail ||
        "Login failed"
      );
    }
    finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-10 flex flex-col gap-4 max-w-md">

      <h1 className="text-2xl font-bold">
        Login
      </h1>

      <input
        className="border p-2"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        className="border p-2"
        placeholder="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button
        onClick={loginUser}
        disabled={loading}
        className="
          border
          border-green-600
          bg-green-600
          text-white
          px-4
          py-2
          rounded-lg
          hover:bg-green-700
          transition
          duration-200
          disabled:bg-gray-400
          disabled:border-gray-400
          disabled:cursor-not-allowed
        "
      >
        {loading ? "Logging in..." : "Login"}
      </button>

      <p>{message}</p>

    </div>
  );
}