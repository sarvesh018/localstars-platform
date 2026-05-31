"use client";

import { useEffect, useState } from "react";

import api from "@/lib/api";

export default function ShopsPage() {

  const [shops, setShops] = useState([]);

  useEffect(() => {

    fetchShops();

  }, []);

  const fetchShops = async () => {

    try {

      const response = await api.get("/shops");

      setShops(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  return (
    <div className="p-10">

      <h1 className="text-3xl font-bold mb-6">
        LocalStars Shops
      </h1>

      <div className="flex flex-col gap-4">

        {shops.map((shop: any) => (

          <div
            key={shop.id}
            className="border p-4 rounded"
          >
            <h2 className="text-xl font-bold">
              {shop.name}
            </h2>

            <p>{shop.category}</p>

            <p>{shop.city}</p>

            <p>
              ⭐ {shop.rating}
            </p>
          </div>
        ))}

      </div>

    </div>
  );
}