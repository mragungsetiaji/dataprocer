import argparse
from dotenv import load_dotenv
from pykg.providers.gcp.operators.dataproc import DataprocOperator
from config import GOOGLE_APPLICATION_CREDENTIALS

def main(action, project_id, region, cluster_name, config_bucket, job_file_path):
 
    client = DataprocOperator(project_id=project_id, 
                              region=region, 
                              cluster_name=cluster_name, 
                              service_account=GOOGLE_APPLICATION_CREDENTIALS, 
                              config_bucket=config_bucket)

    if action=="create_cluster":
        client.create_cluster()
    elif action=="submit_job":
        client.submit_job(job_file_path)
    elif action=="delete_cluster":
        client.delete_cluster()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument("--action", type=str, required=False)
    parser.add_argument("--project_id", type=str, required=False)
    parser.add_argument("--region", type=str, required=False)
    parser.add_argument("--cluster_name", type=str, required=False)
    parser.add_argument("--config_bucket", type=str, required=False)
    parser.add_argument("--job_file_path", type=str, required=False)

    args = parser.parse_args()
    main(args.action, args.project_id, args.region, args.cluster_name, 
         args.config_bucket, args.job_file_path)