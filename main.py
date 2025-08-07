openapi: 3.1.0
info:
  title: Generate Word Report
  description: Create a downloadable Word document for a Level Set coaching profile.
  version: "1.0"
servers:
  - url: https://level-set-profile-builder.onrender.com  # ⬅️ Replace with your real endpoint
paths:
  /generate-docx:
    post:
      operationId: generateWordReport
      summary: Generate Word Profile Document
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                client_name:
                  type: string
                profile_sections:
                  type: object
                  properties:
                    step1:
                      type: string
                    step2:
                      type: string
                    step3:
                      type: array
                      items:
                        type: array
                        items:
                          type: string
                    step4:
                      type: array
                      items:
                        type: array
                        items:
                          type: string
                    step5:
                      type: array
                      items:
                        type: string
                    step6:
                      type: array
                      items:
                        type: array
                        items:
                          type: string
                    summary:
                      type: string
              required:
                - client_name
                - profile_sections
      responses:
        "200":
          description: File download URL
          content:
            application/json:
              schema:
                type: object
                properties:
                  download_url:
                    type: string
rfe
