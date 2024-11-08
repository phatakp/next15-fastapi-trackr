import { auth, currentUser } from "@clerk/nextjs/server";
import { NextResponse } from "next/server";

export async function GET() {
    // Get the userId from auth() -- if null, the user is not signed in
    const { userId, getToken } = await auth();

    const token = await getToken();

    if (!userId) {
        return new NextResponse("Unauthorized", { status: 401 });
    }

    // Get the Backend API User object when you need access to the user's information
    const user = await currentUser();
    const resp = await fetch(`http://localhost:8000/api/v1/auth`, {
        headers: {
            Authorization: `Bearer ${token}`,
        }, // Forward the authorization header
    });
    const data = await resp.json();

    // Perform your Route Handler's logic with the returned user object

    return NextResponse.json({ data }, { status: 200 });
}
