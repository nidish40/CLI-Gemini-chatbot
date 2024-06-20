function helper {
    param (
        
    )

    # Path to the Python script
    $scriptPath = "C:\Users\Nidish\OneDrive\Desktop\Code\projects\Gemini\Learning\CLI-Gemini-chatbot\app.py"

    # Call the Python script with arguments
    & python $scriptPath 
}

# Export the function to make it available in the session
Export-ModuleMember - Function helper
