from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
from datetime import datetime, timezone

# Initialize Flask App and enable CORS
app = Flask(__name__)
CORS(app)

# In-memory data store with some initial sample data
issues = [
    {
        "id": "1",
        "title": "Implement user authentication",
        "description": "Users should be able to sign up and log in.",
        "status": "Open",
        "priority": "High",
        "assignee": "Alice",
        "createdAt": "2025-09-25T10:00:00Z",
        "updatedAt": "2025-09-25T11:30:00Z"
    },
    {
        "id": "2",
        "title": "Fix button styling on the main page",
        "description": "The primary button has incorrect padding.",
        "status": "In Progress",
        "priority": "Medium",
        "assignee": "Bob",
        "createdAt": "2025-09-24T15:00:00Z",
        "updatedAt": "2025-09-25T09:00:00Z"
    },
    {
        "id": "3",
        "title": "Add pagination to the issues list",
        "description": "The main issue list should be paginated to improve performance.",
        "status": "Done",
        "priority": "High",
        "assignee": "Alice",
        "createdAt": "2025-09-23T12:00:00Z",
        "updatedAt": "2025-09-24T18:00:00Z"
    }
]

# Helper function to get the current time in UTC ISO 8601 format
def get_utc_now_iso():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

# --- API Endpoints ---

# GET /health → Health check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

# GET /issues → Get all issues with filtering, sorting, and pagination
@app.route('/issues', methods=['GET'])
def get_issues():
    query_params = request.args
    filtered_issues = list(issues) # Create a copy to modify

    # Search by title (case-insensitive)
    if 'search' in query_params:
        search_term = query_params['search'].lower()
        filtered_issues = [issue for issue in filtered_issues if search_term in issue['title'].lower()]

    # Filtering by exact match
    for key in ['status', 'priority', 'assignee']:
        if key in query_params:
            filter_value = query_params[key]
            filtered_issues = [issue for issue in filtered_issues if issue[key] == filter_value]

    # Sorting
    if 'sortBy' in query_params:
        sort_by = query_params['sortBy']
        sort_order = query_params.get('sortOrder', 'asc')
        reverse = sort_order == 'desc'
        
        if filtered_issues and sort_by in filtered_issues[0]:
             filtered_issues.sort(key=lambda x: x[sort_by], reverse=reverse)

    # Pagination
    page = int(query_params.get('page', 1))
    page_size = int(query_params.get('pageSize', 10))
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    paginated_issues = filtered_issues[start_index:end_index]

    return jsonify({
        "data": paginated_issues,
        "total": len(filtered_issues) # Total count after filtering for pagination UI
    })

# GET /issues/:id → Return single issue
@app.route('/issues/<string:issue_id>', methods=['GET'])
def get_issue(issue_id):
    issue = next((issue for issue in issues if issue['id'] == issue_id), None)
    if issue:
        return jsonify(issue)
    return jsonify({"error": "Issue not found"}), 404

# POST /issues → Create new issue
@app.route('/issues', methods=['POST'])
def create_issue():
    data = request.json
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400

    now = get_utc_now_iso()
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": data['title'],
        "description": data.get('description', ''),
        "status": data.get('status', 'Open'),
        "priority": data.get('priority', 'Medium'),
        "assignee": data.get('assignee', None),
        "createdAt": now,
        "updatedAt": now
    }
    issues.insert(0, new_issue) # Add to the beginning of the list
    return jsonify(new_issue), 201

# PUT /issues/:id → Update issue
@app.route('/issues/<string:issue_id>', methods=['PUT'])
def update_issue(issue_id):
    issue_to_update = next((issue for issue in issues if issue['id'] == issue_id), None)
    if not issue_to_update:
        return jsonify({"error": "Issue not found"}), 404

    data = request.json
    
    # Update fields if they are provided in the request body
    issue_to_update['title'] = data.get('title', issue_to_update['title'])
    issue_to_update['description'] = data.get('description', issue_to_update['description'])
    issue_to_update['status'] = data.get('status', issue_to_update['status'])
    issue_to_update['priority'] = data.get('priority', issue_to_update['priority'])
    issue_to_update['assignee'] = data.get('assignee', issue_to_update['assignee'])
    
    # Refresh the updatedAt timestamp
    issue_to_update['updatedAt'] = get_utc_now_iso()
    
    return jsonify(issue_to_update)

# Main execution block
if __name__ == '__main__':
    app.run(debug=True, port=5000)