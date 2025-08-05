// Global variables to store data between steps
let currentBusinessProfile = null;
let currentNewsItems = null;
let generatedPosts = [];
let postSchedule = [];

// 1. Business Profile
async function getBusinessProfile() {
    const websiteUrl = document.getElementById('website-url').value;
    if (!websiteUrl) {
        showError('business-profile-result', 'Please enter a website URL');
        return;
    }

    try {
        showLoading('business-profile-result');
        const response = await fetch('/api/business-profile', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ website_url: websiteUrl })
        });

        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch profile');
        }
        
        currentBusinessProfile = data;
        displayBusinessProfile(data);
        document.getElementById('content-generation-form').style.display = 'block';
        
    } catch (error) {
        showError('business-profile-result', error.message);
        console.error('Error:', error);
    }
}

function displayBusinessProfile(data) {
    const resultDiv = document.getElementById('business-profile-result');
    resultDiv.innerHTML = `
        <h3>${data.name}</h3>
        <p><strong>Industry:</strong> ${data.industry}</p>
        <p><strong>Services:</strong> ${data.services.join(', ')}</p>
        ${data.description ? `<p><strong>About:</strong> ${data.description}</p>` : ''}
    `;
}

// 2. Industry News
async function getIndustryNews() {
    const industry = document.getElementById('industry').value;
    if (!industry) {
        showError('news-result', 'Please enter an industry');
        return;
    }

    try {
        showLoading('news-result');
        const response = await fetch('/api/industry-news', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ industry })
        });

        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to fetch news');
        }
        
        currentNewsItems = data.news;
        displayIndustryNews(data.news);
        
    } catch (error) {
        showError('news-result', error.message);
        console.error('Error:', error);
    }
}

function displayIndustryNews(newsItems) {
    const resultDiv = document.getElementById('news-result');
    
    if (!newsItems || newsItems.length === 0) {
        resultDiv.innerHTML = '<p>No news found for this industry</p>';
        return;
    }
    
    let html = '<h3>Industry News</h3><div class="news-list">';
    newsItems.forEach(item => {
        const url = item.url || '#';
        html += `
            <div class="news-item">
                <h4><a href="${url}" target="_blank">${item.headline}</a></h4>
                <p>${item.summary || 'No summary available'}</p>
                <small>Source: ${item.source || 'Unknown'}</small>
            </div>
        `;
    });
    html += '</div>';
    
    resultDiv.innerHTML = html;
}

// 3. Content Generation
async function generateContent() {
    if (!currentBusinessProfile) {
        showError('generated-content', 'Please get business profile first');
        return;
    }

    const tone = document.getElementById('tone').value;
    const postType = document.getElementById('post-type').value;

    try {
        showLoading('generated-content');
        const response = await fetch('/api/generate-content', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                business_profile: currentBusinessProfile,
                news_items: currentNewsItems || [],
                preferences: {
                    tone: tone,
                    post_type: postType
                }
            })
        });

        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to generate content');
        }
        
        generatedPosts = data.posts;
        displayGeneratedContent(data.posts);
        document.getElementById('schedule-form').style.display = 'block';
        
    } catch (error) {
        showError('generated-content', error.message);
        console.error('Error:', error);
    }
}

function displayGeneratedContent(posts) {
    const resultDiv = document.getElementById('generated-content');
    
    if (!posts || posts.length === 0) {
        resultDiv.innerHTML = '<p>No content was generated</p>';
        return;
    }
    
    let html = '<h3>Generated Posts</h3><div class="post-list">';
    posts.forEach((post, index) => {
        html += `
            <div class="post" id="post-${index}">
                <p>${post}</p>
                <div class="post-actions">
                    <button class="edit-btn" onclick="editPost(${index})">Edit</button>
                    <button class="delete-btn" onclick="deletePost(${index})">Remove</button>
                </div>
            </div>
        `;
    });
    html += '</div>';
    
    resultDiv.innerHTML = html;
}

// Post Editing Functions
function editPost(index) {
    const postElement = document.getElementById(`post-${index}`);
    const currentText = generatedPosts[index];
    
    postElement.innerHTML = `
        <textarea class="post-edit">${currentText}</textarea>
        <div class="post-actions">
            <button class="save-btn" onclick="savePost(${index})">Save</button>
            <button class="cancel-btn" onclick="displayGeneratedContent(generatedPosts)">Cancel</button>
        </div>
    `;
}

function savePost(index) {
    const editedText = document.querySelector(`#post-${index} .post-edit`).value;
    generatedPosts[index] = editedText;
    displayGeneratedContent(generatedPosts);
}

function deletePost(index) {
    generatedPosts.splice(index, 1);
    displayGeneratedContent(generatedPosts);
}

// 4. Schedule Posts
async function schedulePosts() {
    if (generatedPosts.length === 0) {
        showError('schedule-result', 'Please generate content first');
        return;
    }

    const frequency = document.getElementById('post-frequency').value;

    try {
        showLoading('schedule-result');
        const response = await fetch('/api/schedule-posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                posts: generatedPosts,
                frequency: parseInt(frequency)
            })
        });

        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to schedule posts');
        }
        
        postSchedule = data.schedule;
        displaySchedule(data.schedule);
        
    } catch (error) {
        showError('schedule-result', error.message);
        console.error('Error:', error);
    }
}

function displaySchedule(schedule) {
    const resultDiv = document.getElementById('schedule-result');
    let html = '<h3>Scheduled Posts</h3><div class="schedule-list">';
    
    for (const [day, details] of Object.entries(schedule)) {
        html += `
            <div class="schedule-item">
                <div class="schedule-day"><strong>${day}:</strong></div>
                <div class="scheduled-post">
                    <p>${details.post}</p>
                    <small>Scheduled at: ${details.scheduled_time}</small>
                </div>
            </div>
        `;
    }
    html += '</div>';
    
    resultDiv.innerHTML = html;
}

// 5. Facebook Integration
async function connectFacebook() {
    const pageId = document.getElementById('fb-page-id').value;
    if (!pageId) {
        showError('fb-connection-result', 'Please enter a Facebook Page ID');
        return;
    }

    try {
        showLoading('fb-connection-result');
        const response = await fetch('/api/connect-facebook', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ page_id: pageId })
        });

        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to connect to Facebook');
        }
        
        document.getElementById('fb-connection-result').innerHTML = `
            <p>Status: ${data.status}</p>
            <p>Message: ${data.message}</p>
        `;
        
        if (data.status === 'success') {
            document.getElementById('publish-section').style.display = 'block';
        }
        
    } catch (error) {
        showError('fb-connection-result', error.message);
        console.error('Error:', error);
    }
}

async function publishPosts() {
    if (postSchedule.length === 0) {
        showError('publish-result', 'Please schedule posts first');
        return;
    }

    const pageId = document.getElementById('fb-page-id').value;
    if (!pageId) {
        showError('publish-result', 'Please connect to a Facebook page first');
        return;
    }

    try {
        showLoading('publish-result');
        const response = await fetch('/api/publish-post', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                post_content: generatedPosts[0],  // Publishing first post as example
                page_id: pageId
            })
        });

        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to publish post');
        }
        
        document.getElementById('publish-result').innerHTML = `
            <p>Status: ${data.status}</p>
            <p>Message: ${data.message}</p>
            ${data.post_url ? `<p>Post URL: <a href="${data.post_url}" target="_blank">${data.post_url}</a></p>` : ''}
        `;
        
    } catch (error) {
        showError('publish-result', error.message);
        console.error('Error:', error);
    }
}

// Helper Functions
function showLoading(elementId) {
    document.getElementById(elementId).innerHTML = '<div class="loading">Loading...</div>';
}

function showError(elementId, message) {
    document.getElementById(elementId).innerHTML = `
        <div class="error">${message}</div>
    `;
}

// Initialize form visibility
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('content-generation-form').style.display = 'none';
    document.getElementById('schedule-form').style.display = 'none';
    document.getElementById('publish-section').style.display = 'none';
});