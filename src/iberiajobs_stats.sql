-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: iberiajobs
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `stats`
--

DROP TABLE IF EXISTS `stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats` (
  `Keyword` varchar(256) NOT NULL,
  `FrecuenciaES` int DEFAULT NULL,
  `FrecuenciaUSA` int DEFAULT NULL,
  PRIMARY KEY (`Keyword`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats`
--

LOCK TABLES `stats` WRITE;
/*!40000 ALTER TABLE `stats` DISABLE KEYS */;
INSERT INTO `stats` VALUES ('.NET',4,2),('.NET Core',1,0),('.NET Framework',0,1),('ActionScript',0,0),('ActionScript 3.0',0,0),('Ada',0,0),('Ada 95',0,0),('Adapteva',0,0),('Adobe AIR',0,0),('ADS/Online',0,0),('Advanced Boolean Expression Language',0,0),('Advanced Business Language',0,0),('Agavi',0,0),('Agilent VEE',0,0),('Ajax',1,0),('Akka',0,0),('ALGOL',0,0),('Alice',0,0),('Amazon DynamoDB',0,0),('Amazon Echo/Alexa',0,0),('Amazon Elastic Compute Cloud',0,0),('Amazon RDS',0,0),('Amazon Redshift',0,0),('Amazon Web Services',0,2),('AMD\'s',0,0),('Ametys CMS',0,0),('Android',4,4),('Angular',6,4),('AngularJS',0,1),('AnyChart',0,0),('AOLserver',0,0),('Apache',0,0),('Apache Cassandra',0,0),('Apache HBase',0,0),('Apache Hive',0,0),('Apache Kafka',0,0),('Apache Mesos',0,0),('Apache Spark',0,0),('Apple TV',0,0),('Apple Watch',0,0),('AppScale',0,0),('Arduino',2,0),('ASP.NET',2,2),('AspectJ',0,0),('Assembly',0,0),('Assembly language',0,0),('ATLAS',0,0),('AutoIt',0,0),('AutoLISP',0,0),('Automator',0,0),('Avenue',0,0),('AWK',0,0),('AWS',1,6),('Backbone.js',0,0),('Bash',0,0),('Bash/Shell',0,0),('BASIC',1,0),('Bitcoin',0,0),('Blockchain',1,2),('Bootstrap',1,0),('C',20,10),('C Sharp',1,0),('C shell',0,0),('C-Omega',0,0),('C-Sharp',0,0),('C#',0,0),('C#.NET',1,0),('C++',0,0),('C++/CLI',0,0),('C++03',0,0),('C++0x',0,0),('C++11',0,0),('C++14',0,0),('C++17',0,0),('Cassandra',0,1),('Catalyst',0,0),('Caveman2',0,0),('CBASIC',0,0),('Cecil',0,0),('Chrome extension',0,0),('CLIPS',0,0),('CLIST',0,0),('CLLE',0,0),('Clojure',0,0),('ClojureScript',0,0),('COBOL',1,2),('Cobra',0,0),('COMAL',0,0),('Commodore BASIC',0,0),('Common Lisp',0,0),('Comparison of JavaScript frameworks',0,0),('Compiler Description Language',0,0),('Component Pascal',0,0),('Component-based Scalable Logical Architecture',0,0),('CouchDB',0,0),('cpp',0,0),('Cryptocurrency',0,0),('Crystal',0,0),('CSharp',0,0),('CSharp.NET',0,0),('CSS',3,2),('CubicWeb',0,0),('Cubieboard',0,0),('CUBIT',0,0),('D',8,1),('D3.js',0,0),('Dart',0,0),('DEC Alpha',0,0),('Delphi',0,0),('Delphi.NET',0,0),('Delphi/Object Pascal',0,0),('DirectX High-Level Shading Language',0,0),('DITA',0,0),('Django',2,0),('django CMS',0,0),('dlang',0,0),('Docker',1,0),('ECL',0,0),('ECLiPSe',1,0),('Electron',0,0),('Elixir',0,0),('Ember.js',0,0),('Erlang',0,0),('ES6',0,0),('Ethereum',0,0),('Express',0,0),('Express.js',0,0),('F',1,0),('F Sharp',0,0),('F-Script',0,0),('F-Sharp',0,0),('Fabrik',0,0),('FACT computer language',0,0),('FarCry CMS',0,0),('Fat-Free Framework',0,0),('Fedora Commons',0,0),('FHTML',0,0),('Filetab',0,0),('Firebase',0,0),('Firefox',0,0),('fish',0,0),('FjÃ¶lnir',0,0),('Flask',0,0),('Flexive',0,0),('FLOW-MATIC',0,0),('Fluid UI',0,0),('FOCUS',2,0),('FormEngine',0,0),('FortÃ© TOOL',0,0),('Fortran',0,0),('Fortran 2003',0,0),('Fortran 66',0,0),('Fortran 77',0,0),('Fortran 90',0,0),('Fortran I',0,0),('Foswiki',0,0),('Fox Pro',0,0),('FoxPro',0,0),('FP',2,0),('Freddy II',0,0),('Free Pascal',0,0),('FreeBASIC',0,0),('Freeduino',0,0),('Freemat',0,0),('Freiburger Code',0,0),('FriendlyElec',0,0),('Fril',0,0),('FSharp',0,0),('FuelPHP',0,0),('Furatto',0,0),('Furtive',0,0),('Fusebox',0,0),('Game Maker Language',0,0),('GameMaker Language',0,0),('GameStick',0,0),('Gaming console',0,0),('GAMS',0,0),('Gatsby',0,0),('GAUSS',0,0),('Gawk',0,0),('GDScript',0,0),('Geeklog',0,0),('Gelato\'s Shading Language',0,0),('GeneXus',0,0),('Genie',0,0),('GEORGE',0,0),('GetSimple CMS',0,0),('GFA BASIC',0,0),('Ghost',0,0),('Git',11,0),('GLBasic',0,0),('GNU bison',0,0),('GNU E',0,0),('Go',0,0),('GOAL agent programming language',0,0),('Golang',0,1),('Google App Engine',0,0),('Google Apps Script',0,0),('Google BigQuery',0,0),('Google Closure Tools',0,0),('Google Cloud Platform',0,0),('Google Cloud Storage',0,0),('Google Home',0,0),('Gradle',0,0),('GraphQL',0,0),('Haskell',0,0),('Heroku',0,0),('Homebrew',0,0),('Homebridge',0,0),('HTML',4,1),('IBM BASICA',0,0),('IBM Cloud',0,0),('IBM Db2',0,0),('IBM Informix-4GL',0,0),('IBM NetRexx',0,0),('IBM RPG',0,0),('IBM System/360',0,0),('IBM VisualAge',0,0),('IBM Watson',0,0),('IBM WebSphere Application Server',0,0),('IBM WebSphere Application Server Community Edition',0,0),('ICEfaces',0,0),('ICI',0,0),('ICub',0,0),('IDL',0,0),('IGEPv2',0,0),('IGOR Pro',0,0),('IITRAN',0,0),('Ikiwiki',0,0),('ILERPG',0,0),('ImpressCMS',0,0),('ImpressPages',0,0),('Impulse C',0,0),('INEK',0,0),('Information Processing Language',0,0),('Ink',0,0),('Integer BASIC',0,0),('Intel',0,0),('Intel 80186',0,0),('Intel 80286',0,0),('Intel 8086',0,0),('Intel Galileo',0,0),('Intel\'s',0,0),('Interlisp',0,0),('Internal Translator',0,0),('International Federation for Information Processing',0,0),('Inuit CSS',0,0),('iOS',1,4),('IPFS',0,0),('J',4,0),('J#',0,0),('JADE',0,0),('Java',8,14),('Java Platform, Enterprise Edition',0,0),('JavaCC',0,0),('JavaFX',0,0),('JavaFX Script',0,0),('JavaPoly',0,0),('JavaScript',10,4),('JavaServer Faces',0,0),('Jekyll',0,0),('jQuery',5,1),('jQuery Mobile',0,0),('jQuery UI',0,0),('jQWidgets',0,0),('JS',4,3),('JS++',0,0),('JScript',0,0),('JScript.NET',0,0),('JSL',0,0),('JSON',2,1),('JsPHP',0,0),('JsRender/JsViews',0,0),('Julia',0,0),('Jupyter',0,0),('Kotlin',0,1),('Kubernetes',1,1),('LaTeX',0,0),('Linux',4,2),('Lisp',0,0),('Logo',0,0),('Lua',0,0),('Mac OS',0,1),('macOS',0,0),('Mainframe',0,1),('MariaDB',0,0),('Markdown',0,0),('Mastodon',0,0),('Material design',1,0),('MATLAB',1,0),('Maven',1,0),('Memcached',0,0),('Microsoft Azure',0,0),('Monero',0,0),('MongoDB',0,1),('Mongoose',0,0),('MvvmCross',0,0),('MySQL',4,0),('NativeScript',0,0),('Neo4j',0,0),('Nim',0,0),('Node.js',0,2),('NoSQL',0,2),('Objective-C',0,1),('OCaml',0,0),('Open Programming Language',0,0),('Open Semantic Framework',0,0),('Open Shading Language',0,0),('OpenCart',0,0),('OpenCms',0,0),('OpenEdge',0,0),('Openframe',0,0),('OpenGL',0,0),('OpenGL Shading Language',0,0),('OpenKM',0,0),('OpenLaszlo',0,0),('OpenLisp',0,0),('Openmoko',0,0),('OpenPOWER',0,0),('OpenRasta',0,0),('OpenRAVE',0,0),('OpenROAD',0,0),('OpenROV',0,0),('OpenSPARC',0,0),('OpenWGA',0,0),('OpenXava',0,0),('OPS5',0,0),('OptimJ',0,0),('Oracle',7,5),('Oracle Application Development Framework',0,0),('Oracle Application Express',0,0),('Oracle Database',0,0),('Oracle Forms',0,0),('Oracle Reports',0,0),('p5.js',0,0),('Pascal',0,0),('PDF.js',0,0),('Perl',0,1),('Perl 6',0,0),('Perl Data Language',0,0),('Perl language structure',0,0),('Ph7cms',0,0),('Phalcon',0,0),('Phaser',0,0),('Phire CMS',0,0),('Phoenix',0,0),('PHP',5,1),('PHP Unit Testing Framework',0,0),('PHP-Nuke',0,0),('PhpCodeGenie',0,0),('PHPRunner',0,0),('PHPUnit',0,0),('phpWebLog',0,0),('phpWiki',0,0),('PICO-8',0,0),('Pixi.js',0,0),('PL/I',0,0),('PL/SQL',4,1),('PlayStation',0,0),('Plotly',0,0),('Polymer',0,0),('PostgreSQL',3,0),('PostScript',0,0),('PowerBASIC',0,0),('PowerScript',0,0),('PowerShell',0,1),('Predix',0,0),('Processing',1,0),('Processing.js',0,0),('Prolog',0,0),('PROSE modeling language',0,0),('Prototype JavaScript Framework',0,0),('PS',0,0),('Pure',0,0),('Pure CSS',0,0),('PWA',0,0),('PWCT',0,0),('Pyjs',0,0),('Pylons',0,0),('Python',5,5),('PyTorch',0,0),('Qt',2,0),('QUnit',0,0),('R',1,0),('Rails',0,0),('Raspberry Pi',1,0),('Ratchet',0,0),('React',7,10),('React Fiber',0,0),('React Native',1,2),('React.js',0,1),('ReactiveUI',0,0),('READ/PRINT',0,0),('Reaktor',0,0),('REALbasic',0,0),('Redis',0,0),('Redux',0,0),('REFAL',0,0),('Refinery CMS',0,0),('Regional Assembly Language',0,0),('Remote Application Platform',0,0),('RenderMan Shading Language',0,0),('REST',8,3),('REST API',0,1),('RPG',0,0),('RPL',0,0),('Ruby',1,0),('Ruby on Rails',0,0),('Run BASIC',0,0),('Rust',1,0),('Rustlang',0,0),('Salesforce',0,5),('SAS',0,0),('Sass',0,0),('Scala',1,0),('Scheme',0,0),('scikit-learn',0,0),('Scratch',0,2),('Serverless',0,0),('SETL',0,0),('sh',0,0),('SharePoint',0,1),('Shell',1,0),('Sketch',0,0),('Solidity',0,0),('Spring',5,1),('Spring Boot',1,0),('SQL',14,7),('SQL Server',5,0),('SQLite',1,0),('Standard ML',0,0),('Storybook',0,0),('Swift',2,2),('Symfony',1,0),('Tcl',0,0),('Telegram',0,0),('TensorFlow',0,0),('Terminal',0,0),('Terraform',0,0),('Three.js',1,0),('Topcoat',0,0),('Torch',0,0),('Total.js',0,0),('Transact-SQL',0,0),('Twig.js',0,0),('TypeScript',1,1),('Ubuntu',0,0),('Underscore.js',0,0),('Unit.js',0,0),('Unity',2,0),('Unreal Engine',0,0),('Vagrant',0,0),('VB.NET',1,0),('VBA',0,0),('Velocity.js',0,0),('Verge3D',0,0),('Vim',0,0),('VisiCalc',0,0),('VisSim',0,0),('Visual Basic',0,0),('Visual Basic .NET',0,0),('Visual Basic.NET',0,0),('Visual DataFlex',0,0),('Visual FoxPro',0,0),('Visual Prolog',0,0),('VisualWorks',0,0),('Vue.js',1,1),('Web Components',0,0),('Webpack',1,0),('Western Design Center',0,0),('Whiley',0,0),('Whirlwind assembler',0,0),('Wiki.js',0,0),('Winbatch',0,0),('Windows',4,0),('Windows batch language',0,0),('Windows Desktop',1,0),('Windows Phone',0,0),('Windows PowerShell',0,0),('Windows Server',0,0),('WinSystems, Inc',0,0),('WordPlate',0,0),('WordPress',0,1),('x86',0,0),('x86-64',0,0),('XAML',0,0),('Xbox',0,0),('XML',2,1),('YAML',0,0),('Z shell',0,0);
/*!40000 ALTER TABLE `stats` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-13 19:15:44
