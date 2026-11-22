
let pipeline = [];


function updatePipelineDisplay() {

    document.getElementById("pipelineDisplay").textContent =
        JSON.stringify(pipeline, null, 4);
}


function addStage() {

    const stageName =
        document.getElementById("stage").value;

    const configuration =
        document.getElementById("configuration").value;

    try {

        const parsedConfiguration =
            JSON.parse(configuration);

        pipeline.push({
            [stageName]: parsedConfiguration
        });

        updatePipelineDisplay();

        document.getElementById("status").textContent =
            "Stage added successfully.";

    } catch (error) {

        document.getElementById("status").textContent =
            "Invalid JSON configuration.";

    }
}


async function executePipeline() {

    const collection =
        document.getElementById("collection").value;

    if (pipeline.length === 0) {

        document.getElementById("status").textContent =
            "Please add at least one stage.";

        return;
    }

    document.getElementById("status").textContent =
        "Executing pipeline...";

    try {

        const response = await fetch("/execute", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                collection: collection,
                pipeline: pipeline
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Execution failed.");
        }

        document.getElementById("status").textContent =
            "Pipeline executed successfully.";

        document.getElementById("resultCount").textContent =
            data.result_count;

        document.getElementById("results").textContent =
            JSON.stringify(data.results, null, 4);

    } catch (error) {

        document.getElementById("status").textContent =
            "Error: " + error.message;

        document.getElementById("resultCount").textContent =
            "0";

        document.getElementById("results").textContent =
            "No results available.";

    }
}


function clearPipeline() {

    pipeline = [];

    updatePipelineDisplay();

    document.getElementById("results").textContent =
        "No results available.";

    document.getElementById("resultCount").textContent =
        "0";

    document.getElementById("status").textContent =
        "Pipeline cleared.";

}


updatePipelineDisplay();
