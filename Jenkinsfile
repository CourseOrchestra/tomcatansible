node {
   stage ("Get Latest Code") {
      checkout scm
   }
   
   try {
     stage ("Molecule test") {
        /* Jenkins check out the role into 
        a folder with arbitrary name, so we need to
        let Ansible know where to find 'tomcatansible' role*/
        sh 'mkdir -p molecule/default/roles'
        sh 'ln -sf `pwd` molecule/default/roles/tomcatansible'
        sh 'molecule test'
     }
   } catch(all) {
      currentBuild.result = "FAILURE"
      throw err
   }
}